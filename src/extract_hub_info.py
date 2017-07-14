from github import Github
import os
from PIL import Image
import requests
import math
from snakemake.utils import makedirs
import random
import datetime
import matplotlib.pyplot as plt
from dateutil.relativedelta import relativedelta
import pandas as pd
import base64
from geopy.geocoders import Nominatim
from lxml import etree
import json


configfile: "config.yaml"

# connect to GitHub
g = Github(config["github"])
# retrieve the hub repository
hub_repo = g.get_user("galaxyproject").get_repo("galaxy-hub")
# create a geolocator instance
geolocator = Nominatim()


def format_date(date):
    '''
    Format date to put it at the begin of the day
    '''
    first_day = date.replace(hour = 0)
    first_day = first_day.replace(minute = 0)
    first_day = first_day.replace(second = 1)
    return first_day


rule all:
    input:
        gtn_event_tab = "data/gtn_events.csv",
        gtn_event_map = "images/gtn_events.geojson",
        gtn_event_graph = "images/gtn_events.png"


def extract_line(keyword, string):
    '''
    Extract the line for a key word in a string with multiple line
    '''
    pos = string.find(keyword)
    return string[pos:].split("\n")[0]


def extract_info(string):
    '''
    Extract the useful information of a string
    '''
    if string.find(":") == -1:
        return ""
    return string.rstrip().split(": ")[1]


def extract_location_details(location):
    '''
    Extract the latitude and longitude of a location
    '''
    if location is None:
        return (None, None)
    loc = geolocator.geocode(location)
    while len(location) > 0 and loc is None:
        location = ", ".join(location.split(", ")[1:])
        loc = geolocator.geocode(location)
    if loc is not None:
        return (loc.latitude, loc.longitude)
        latitude = loc.latitude
        longitude = loc.longitude
    else:
        return (None, None)


def parse_hierarchy(element):
    '''
    Parse the element hierarchically to extract information
    '''
    text = ''
    gtn_event = False
    for subel in element:
        # parse the subelements
        if len(subel.getchildren()) == 0:
            text = subel.text
            if subel.tag == "img":
                if 'alt' in subel.attrib and subel.attrib['alt'].find("GTN") != -1:
                    gtn_event = True
        else:
            (subel_text, subel_gtn_event) = parse_hierarchy(subel)
            # conserve the text of the first child
            if text == '':
                text = subel_text
            gtn_event |= subel_gtn_event        
    return text, gtn_event


def extract_date(date_string):
    '''
    Format the date
    '''
    return datetime.datetime.strptime(date_string, "%B %d %Y")


def extract_archived_event_info(file_content):
    '''
    Extract the useful event information for the archived events
    '''
    file_content = file_content.decode("utf-8")
    # find the first year line
    year_pos = [m.start() for m in re.finditer('## ', file_content)]
    events = {}
    for i, pos in enumerate(year_pos):
        # extract the lines with info about the year
        if i < len(year_pos) - 1:
            next_pos = year_pos[i+1]
        else:
            next_pos = -1
        year_info = file_content[pos:next_pos]
        # extract year
        year = year_info.split("\n")[0].split("## ")[1]
        # extract the substring with the event table
        start_table = year_info.find("<table")
        end_table = year_info.find("</table>") + len("</table>")
        event_table_str = year_info[start_table:end_table]
        # format it for lxml
        table = etree.HTML(event_table_str).find("body/table")
        # parse it
        rows = iter(table)
        headers = [col.text[1:-1] for col in next(rows)]
        # parse the events
        for row in rows:
            values = []
            gtn_event = False
            # parse the col
            for col in row:
                text = col.text[1:-1]
                if len(text) == 0:
                    # parse hierarchy
                    text, col_gtn_event = parse_hierarchy(col)
                    gtn_event |= col_gtn_event
                values.append(text)
            if not gtn_event:
                continue
            if len(values) < 4:
                continue
            # link the info to the headers of the table
            info = dict(zip(headers, values))
            # extract the info
            date = info["Date"]
            title = info["Topic/Event"]
            location = info["Venue/Location"]
            name = title.lower().replace(' ', '_')
            # format the date and extract the duration
            days = 1
            if date.find('-') != -1:
                original_date = date
                pos = date.find('-')
                date = date[:pos].rstrip()
                # extract the number of days
                if original_date.find(' -') == -1:
                    str_days = original_date.split(' ')[1].split('-')
                    days = int(str_days[1]) - int(str_days[0])
                else:
                    str_days = original_date.split(' - ')
                    start = extract_date("%s %s" %(str_days[0], year))
                    end = extract_date("%s %s" %(str_days[1], year))
                    days = (end - start).days
            elif date.find(',') != -1:
                pos = date.find(',')
                days = date.count(',') + 1
                date = date[:pos].rstrip()
            date = extract_date("%s %s" %(date, year))
            # extract location
            (latitude, longitude) = extract_location_details(location)
            # save the events
            events[name] = [title, date, days, latitude, longitude]
    return events


def extract_event_info(file_content):
    '''
    Extract the useful event information for an event with a page on the hub
    '''
    # extracting the interesting lines
    title_line = extract_line("title", file_content)
    date_line = extract_line("date", file_content)
    days_line = extract_line("days", file_content)
    location_line = extract_line("location", file_content)
    gtn_line = extract_line("gtn", file_content)    
    # extract information
    title = extract_info(title_line)
    date = extract_info(date_line)[1:-1]
    days = extract_info(days_line)
    location = extract_info(location_line)
    # format the date
    date = datetime.datetime.strptime(date, "%Y-%m-%d")
    # format the day
    if days != '':
        days = int(days)
    else:
        days = 1
    # extract location
    (latitude, longitude) = extract_location_details(location)
    return (title, date, days, latitude, longitude)


rule extract_gtn_events:
    '''
    Extract the number of GTN events over the months
    '''
    output:
        gtn_event_tab = "data/gtn_events.csv"
    run:
        # create an empty data frame
        df = pd.DataFrame(
            0,
            columns=["title","date","days","loc_latitude","loc_longitude"],
            index=[])
        # parse the events
        for content in hub_repo.get_dir_contents("src/events"):
            path = content.path
            name = content.name
            if name.find(".") != -1:
                continue
            for file in hub_repo.get_dir_contents(path):
                # parsing only the index.md files
                if file.name != "index.md":
                    continue
                # extracting the file content
                file_content = base64.b64decode(file.content)
                # extract the event info
                if name == "archive":
                    archived_events = extract_archived_event_info(file_content)
                    for event in archived_events:
                        df.loc[event] = archived_events[event]
                else:
                    file_content = file_content.decode("utf-8")
                    if file_content.find("gtn: y") == -1:
                        continue
                    (title, date, days, latitude, longitude) = extract_event_info(file_content)
                    # add a row with the information
                    df.loc[name] = [title, date, days, latitude, longitude]
        # export to file
        df.to_csv(
            str(output.gtn_event_tab),
            index = True)


def format_str_date(date_str):
    '''
    Take a date as a string and reformat it to get the month and year as a string
    '''
    #date = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    #return "{:%B %Y}".format(date)
    return datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")


rule generate_event_map:
    '''
    Generate the event map
    '''
    input:
        gtn_event_tab = "data/gtn_events.csv"
    output:
        gtn_event_map = "images/gtn_events.geojson"
    run:
        # load the event info
        df = pd.read_csv(str(input.gtn_event_tab), index_col = 0)
        # initiate the dict for the map
        json_map = {
            "type": "FeatureCollection",
            "features": []}
        # parse the events
        for index, row in df.iterrows():
            # pass if there is no coordinates
            if pd.isnull(row['loc_latitude']):
                continue
            # add the event to the map
            json_map["features"].append({
                "type": "Feature",
                "geometry": {
                  "type": "Point",
                  "coordinates": [row['loc_longitude'], row['loc_latitude']]},
                "properties": {
                  "Event": row['title'],
                  "Date": format_str_date(row['date']).strftime("%B %d, %Y"),
                  "Duration": row['days']}})
        # export dict to JSON
        with open(str(output.gtn_event_map), 'w') as fp:
            json.dump(json_map, fp)


rule plot_gtn_events:
    '''
    Plot the number of GTN events over the month
    '''
    input:
        gtn_event_tab = "data/gtn_events.csv"
    output:
        gtn_event_graph = "images/gtn_events.png"
    run:
        # load the event info
        df = pd.read_csv(str(input.gtn_event_tab), index_col = 0)
        # format the date
        new_df = df['date'].map(format_str_date).to_frame()
        new_df.index = new_df['date']
        # group by month
        grouped_date = new_df.groupby(pd.TimeGrouper("M")).count()
        # plot the number of events per month
        fig = plt.plot()
        ax = grouped_date.date.plot(
            kind='bar',
            title='Number of registered GTN training events over the months')
        ax.set_xlabel('')
        #ax.xaxis_date()
        xtl=[item.get_text()[:7] for item in ax.get_xticklabels()]
        ax.set_xticklabels(xtl)

        plt.tight_layout()
        plt.savefig(str(output.gtn_event_graph))
