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


def format_str_date(date_str):
    '''
    Take a date as a string and reformat it to get the month and year as a string
    '''
    #date = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    #return "{:%B %Y}".format(date)
    return datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")


def format_date(date):
    '''
    Format date to put it at the begin of the month
    '''
    first_day = date.replace(day = 1)
    first_day = first_day.replace(hour = 0)
    first_day = first_day.replace(minute = 0)
    first_day = first_day.replace(second = 1)
    return first_day


def extract_resizing_value(x, y, n):
    '''
    Extracting the resizing value using the algo in
    https://math.stackexchange.com/questions/466198/algorithm-to-get-the-maximum-size-of-n-squares-that-fit-into-a-rectangle-with-a

    x: width of the rectangle
    y: height of the rectangle
    n: number of square to fit in the (x,y) rectangle
    '''
    px = math.ceil(math.sqrt(n*x/y))
    py = math.ceil(math.sqrt(n*y/x))
    if math.floor(px*y/x)*px < n:
        sx = y/math.ceil(px*y/x)
    else:
        sx = x/px
    if math.floor(py*x/y)*py < n:
        sy = x/math.ceil(x*py/y)
    else:
        sy = y/py
    return math.floor(max(sx, sy))


configfile: "config.yaml"

# connect to GitHub
g = Github(config["github"])
# extract the Galaxy Training Material repository
training_repo = g.get_user("galaxyproject").get_repo("training-material")
#creation_date = training_repo.created_at
# creation date at GCC2016
creation_date = format_str_date("2016-06-01 00:00:01")
# generate a data range with month (first day of the month)
data_range = pd.date_range(
    format_date(creation_date),
    format_date(datetime.datetime.now() + relativedelta(months=1)),
    freq=pd.tseries.offsets.DateOffset(months=1))

bg_col = (config["bg_col"]["r"], config["bg_col"]["g"], config["bg_col"]["b"])

rule all:
    input:
        contributors="images/contributors.png",
        contribution_graph = "images/contributions.png",
        new_contributor_graph = "images/contributor_nb.png"


rule extract_contributor_avatar:
    '''
    Create an image composed of the avatar of all the contributors
    '''
    output:
        contributors="images/contributors.png"
    run:
        avatar_paths = []
        avatar_dir = os.path.join("images", "avatars")
        makedirs(avatar_dir)
        # parse the contributors
        for contri in training_repo.get_contributors():
            # get the url to the avatar
            avatar_url = contri.avatar_url
            # download the avatar with requests
            avatar_path = os.path.join(avatar_dir, "%s.png" % contri.login)
            if not os.path.exists(avatar_path):
                r = requests.get(avatar_url, stream=True)
                r.raise_for_status()
                with open(avatar_path, "ab") as fd:
                    for chunk in r.iter_content(chunk_size=128):
                        fd.write(chunk)
            # add the path to the list of image paths
            avatar_paths.append(avatar_path)
        # create image to combine the avatars
        result = Image.new("RGB", (config["width"], config["height"]))
        # extract the resizing value
        img_nb = len(avatar_paths)
        print("img nb: %s" % img_nb)
        new_size = extract_resizing_value(
            config["width"],
            config["height"],
            img_nb)
        print("new size: %s" % new_size)
        # extract the number of row and number of column
        col_nb = math.floor(config["width"] / new_size)
        row_nb = math.floor(config["height"] / new_size)
        print("col: %s, row: %s" % (col_nb, row_nb))
        # compute extra pixels
        extra_left_right_pixels = config["width"] - col_nb*new_size
        extra_top_down_pixels = config["height"] - row_nb*new_size
        print("top-down: %s, left-right: %s" % (extra_top_down_pixels, extra_left_right_pixels))
        d_left = math.ceil(extra_left_right_pixels/2)
        d_top = math.ceil(extra_top_down_pixels/2)
        # find how many rectangles will be empty
        empty_rect_nb = col_nb*row_nb - img_nb
        # add as many empty path as many empty rectangles
        avatar_paths += [""] * empty_rect_nb
        # randomize the list of path
        random.shuffle(avatar_paths)
        # resize and add avatar
        for index, filename in enumerate(avatar_paths):
            # if empty path: add nothing
            if not os.path.exists(filename):
                continue
            # load and resize the image
            img = Image.open(filename)
            resized_img = img.resize((new_size, new_size))
            # extract the position of the image in the rectangle
            x = index // row_nb * new_size + d_left
            y = index % row_nb * new_size + d_top
            # add the image
            result.paste(resized_img, (x, y, x + new_size, y + new_size))
        # export the image
        result.save(str(output.contributors))


rule extract_contribution_number:
    '''
    Extract the number of contributions (commits, PR and issues) over the months
    '''
    output:
        contribution_tab = "data/contributions.csv"
    run:
        # extract the contributions per months
        df = pd.DataFrame(
            0,
            columns=["commit_nb","pull_request", "issue"],
            index=data_range)
        # extract the number of commits
        for commit in training_repo.get_commits():
            date = format_date(commit.commit.author.date)
            df.iloc[df.index.get_loc(date, method='nearest')].commit_nb += 1
        # extract the number of Pull Requests (all: open and closed ones)
        for pr in training_repo.get_pulls(state="all"):
            date = format_date(pr.created_at)
            df.iloc[df.index.get_loc(date, method='nearest')].pull_request += 1
        # extract the number of Issues (all: open and closed ones)
        for issue in training_repo.get_issues(state="all"):
            # not counting the issues that are PR
            if issue.pull_request is not None:
                continue
            date = format_date(issue.created_at)
            df.iloc[df.index.get_loc(date, method='nearest')].issue += 1
        # export to file
        df.to_csv(
            str(output.contribution_tab),
            index = True)


rule plot_contribution_number:
    '''
    Plot the number of contributions (commits, PR and issues) over the months
    '''
    input:
        contribution_tab = "data/contributions.csv"
    output:
        contribution_graph = "images/contributions.png"
        #contribution_graph_with_hackathon = "images/contributions_with_hackathon.png"
    run:
        # load the contribution number
        df = pd.read_csv(str(input.contribution_tab), index_col = 0)
        # rename the row and columns
        df.index = df.index.map(format_str_date)
        df = df.rename(columns = {
            "commit_nb": "Commits",
            "pull_request": "Pull Requests",
            "issue": "Issues"})
        # without hackathons
        # plot the number of contributions
        fig = plt.plot()
        ax = df.plot(x_compat=True)
        # add vertical line for GCC 2016
        #plt.axvline(
        #    x=format_str_date("2016-06-01 00:00:01"),
        #    color='k',
        #    linestyle='--',
        #    linewidth=2)
        plt.tight_layout()
        ax.set_facecolor(bg_col)
        plt.savefig(str(output.contribution_graph), facecolor=bg_col, transparent=True)
        # with hackathons
        # plot the number of contributions
        #fig = plt.plot()
        #ax = df.plot(x_compat=True)
        ## add vertical line for the contribution fests
        ##plt.axvline(
        ##    x=format_str_date("2016-10-01 00:00:01"),
        ##    color='r',
        ##    linestyle='--')
        ##plt.axvline(
        ##    x=format_str_date("2017-05-01 00:00:01"),
        ##    color='r',
        ##    linestyle='--')
        ##plt.axvline(
        ##    x=format_str_date("2017-06-01 00:00:01"),
        ##    color='r',
        ##    linestyle='--')
        ### add contribution fest date
        ##plt.text(
        ##    format_str_date("2016-10-01 00:00:01"),
        ##    max(df.max()),
        ##    "Online\nContribution\nFest",
        ##    horizontalalignment='left',
        ##    verticalalignment='top')
        ##plt.text(
        ##    format_str_date("2017-05-01 00:00:01"),
        ##    max(df.max()),
        ##    "Cambridge\nTraining\nHackathon",
        ##    horizontalalignment='right',
        ##    verticalalignment='top')
        ##plt.text(
        ##    format_str_date("2017-06-01 00:00:01"),
        ##    max(df.max()),
        ##    "GCC\nHackathon",
        ##    horizontalalignment='left',
        ##    verticalalignment='top')
        ## export the figure
        #plt.tight_layout()
        #ax.set_facecolor(bg_col)
        #plt.savefig(str(output.contribution_graph_with_hackathon), facecolor=bg_col, transparent=True)


rule extract_contributor_number:
    '''
    Extract the number of contributors over the months
    '''
    output:
        contributor_tab = "data/contributors.csv"
    run:
        # extract the contributors per months
        df = pd.DataFrame(
            0,
            columns=["first_contribution"],
            index=data_range)
        # parse the contributors
        for contri in training_repo.get_contributors():
            # extract the first commit by parsing the commits
            first_commit = datetime.datetime.now()
            commit_number = 0 
            for commit in training_repo.get_commits(author=contri):
                commit_date = commit.commit.author.date
                if commit_date < first_commit:
                    first_commit = commit_date
            # add the a value for this date
            date = format_date(first_commit)
            df.iloc[df.index.get_loc(date, method='nearest')].first_contribution += 1
        # export to file
        df.to_csv(
            str(output.contributor_tab),
            index = True)


rule plot_contributor_number:
    '''
    Plot the number of new contributors over the months
    '''
    input:
        contributor_tab = "data/contributors.csv"
    output:
        contributor_graph = "images/contributor_nb.png"
    run:
        # load the contribution number
        df = pd.read_csv(str(input.contributor_tab), index_col = 0)
        # rename the row and columns
        df.index = df.index.map(format_str_date)
        # plot the number of contributions
        fig = plt.plot()
        ax = df.first_contribution.cumsum().plot(
            x_compat=True,
            title="Number of contributors")
        # fit the plot to the figure
        plt.tight_layout()
        ax.set_facecolor(bg_col)
        plt.savefig(str(output.contributor_graph), facecolor=bg_col, transparent=True)

rule 