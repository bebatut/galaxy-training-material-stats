import base64
import matplotlib.pyplot as plt
import pandas as pd
import yaml

from github import Github
from pprint import pprint


configfile: "config.yaml"

# connect to GitHub
g = Github(config["github"])
# retrieve the hub repository
repo = g.get_user("galaxyproject").get_repo("training-material")

date = "15.06.18"


rule all:
    input:
        repo_content = "data/current_repo_content",
        repo_content_stats = "data/repo_content_stats",
        repo_content_stat_plot = "images/repo_content_stat_plot.png",
        tech_support_stat_plot = "images/tech_support_stat_plot.png",
        tech_support_prop_plot = "images/tech_support_prop_plot.png"


def get_yaml_content(file_content):
    '''
    Extract the YAML content of the file from GitHub

    :param file_content: the encoded content of the file obtained with GitHub API

    :return: content in YAML of the file
    '''
    decoded_file_content = base64.b64decode(file_content)
    yaml_content = yaml.load(decoded_file_content)
    return yaml_content


def extract_training_content(ref):
    '''
    Extract the details about the current resources in the Galaxy Training Material

    :param ref: name of the commit/branch/tag

    :return: dictionary with information about the tutorials in each topic on ref
    '''
    trainings = {}
    for file in repo.get_dir_contents("metadata", ref):
        # get only topics
        if file.name == "contributors.yaml" or file.name == "instances.yaml":
            continue
        yaml_content = get_yaml_content(file.content)
        # get topic tutorial
        topic = yaml_content['title']
        trainings.setdefault(topic, {})
        for tuto in yaml_content['material']:
            tuto_name = tuto['title']
            # skip introduction and not stable tutorials
            if tuto['type'] == 'introduction':
                continue
            if 'enable' in tuto and tuto['enable'] == 'false':
                continue
            trainings[topic].setdefault(tuto_name, {})
            # collect information from the metadata.yaml file
            infos = ['hands_on', 'slides', 'galaxy_tour', 'workflows', 'zenodo_link']
            for info in infos:
                if info in tuto:
                    trainings[topic][tuto_name][info] = tuto[info]
                else:
                    trainings[topic][tuto_name][info] = False
            # collect the tool.yaml, data_library.yaml file
            tuto_path = "topics/%s/tutorials/%s" %(yaml_content['name'], tuto['name'])
            trainings[topic][tuto_name]['tools'] = False
            trainings[topic][tuto_name]['data_library'] = False
            for tuto_file in repo.get_dir_contents(tuto_path, ref):
                if tuto_file.name == 'data-library.yaml':
                    decoded_file_content = base64.b64decode(tuto_file.content)
                    if "Small file (to change)" in str(decoded_file_content) or "Small test files" in str(decoded_file_content):
                        continue
                    trainings[topic][tuto_name]['data_library'] = True
                elif tuto_file.name == 'tools.yaml':
                    decoded_file_content = base64.b64decode(tuto_file.content)
                    if "Where to put the tool" in str(decoded_file_content):
                        continue
                    trainings[topic][tuto_name]['tools'] = True
    return trainings


rule extract_repo_content:
    '''
    Extract the details about the current resources in the Galaxy Training Material
    '''
    output:
        after_one_year_repo_content = "data/after_one_year_repo_content",
        current_repo_content = "data/current_repo_content"
    run:
        # after one year
        after_one_year_training = extract_training_content("44164c9b")
        stream = open(str(output.after_one_year_repo_content), 'w')
        yaml.dump(after_one_year_training, stream)
        # current
        current_training = extract_training_content("master")
        stream = open(str(output.current_repo_content), 'w')
        yaml.dump(current_training, stream)


def extract_training_stats(ref):
    '''
    Extract the details about the current resources in the Galaxy Training Material

    :param ref: name of the commit/branch/tag

    :return: dictionary with some statistics about the training content on ref
    '''
    stats = pd.DataFrame({'topics': 0,
                          'tutorials': 0,
                          'hands_on': 0,
                          'slides': 0,
                          'galaxy_tour': 0,
                          'workflows': 0,
                          'zenodo_link': 0,
                          'tools': 0,
                          'data_library': 0},
                          index=[ref])
    content = extract_training_content(ref)
    # extract stats
    hands_on_info = ["tools", "galaxy_tour", "workflows", "zenodo_link", "data_library"]
    no_hands_on_topic = ["Development in Galaxy", "Contributing to the Galaxy Training Material", "Train the trainers", "Galaxy Server administration"]
    for topic in content:
        stats.loc[ref,'topics'] += 1
        for tuto in content[topic]:
            stats.loc[ref,'tutorials'] += 1
            for info in list(stats.columns):
                if info in content[topic][tuto]:
                    if content[topic][tuto][info]:
                        if info in hands_on_info and topic in no_hands_on_topic:
                            continue
                        if content[topic][tuto][info] == "no":
                            continue
                        if content[topic][tuto][info] == "external":
                            continue
                        if content[topic][tuto][info] == "url to Zenodo with input data":
                            continue
                        stats.loc[ref,info] += 1
                    elif info in hands_on_info and topic not in no_hands_on_topic:
                        print("%s - %s (%s)" % (topic, tuto, ref))
    # reindex
    stats = stats[['topics','tutorials','hands_on','slides','tools','workflows','zenodo_link','data_library','galaxy_tour']]
    # rename columns
    stats = stats.rename(columns={"topics":"Topics",
                                  "tutorials":"Tutorials",
                                  "hands_on":"Hands-on",
                                  "slides":"Slide decks",
                                  "tools": "Tools",
                                  "workflows": "Worflows",
                                  "zenodo_link": "Data on Zenodo",
                                  "data_library": "Data for data libraries",
                                  "galaxy_tour": "Interactive tours"})
    return stats


rule extract_repo_content_stat:
    '''
    Extract some stats about the evolution of the resources in the Galaxy Training Material
    '''
    output:
        repo_content_stats = "data/repo_content_stats"
    run:
        # extract stats
        after_one_year_training = extract_training_stats("44164c9b")
        current_training = extract_training_stats("master")
        # combine stats
        all_stats = pd.concat([after_one_year_training, current_training])
        all_stats = all_stats.rename(index={"44164c9b":"22.06.17","master":date})
        # export to csv
        all_stats.to_csv(
            str(output.repo_content_stats),
            index = True)


rule plot_content_stat:
    '''
    Plot number of topics, tutorials, etc
    '''
    input:
        repo_content_stats = "data/repo_content_stats"
    output:
        repo_content_stat_plot = "images/repo_content_stat_plot.png"
    run:
        # load stats
        all_stats = pd.read_csv(str(input.repo_content_stats), index_col = 0)
        content_stats = all_stats[["Topics", "Tutorials", "Hands-on", "Slide decks"]].transpose()
        # plot barplot stats
        fig = plt.plot()
        ax = content_stats.plot(kind='bar', legend=True, fontsize=12, color=["orange","darkblue"], title="Number in the repository")
        ax.set_xticklabels(content_stats.index, rotation=45)
        plt.tight_layout()
        plt.savefig(str(output.repo_content_stat_plot), transparent=True)
        # extract proportions
        prop = pd.DataFrame({'Both hands-on and slide deck': 0,
                             'Only hands-on': 0,
                             'Only slide deck': 0},
                             index=all_stats.index)
        prop['Both hands-on and slide deck'] = (all_stats['Hands-on'] + all_stats['Slide decks'] - all_stats['Tutorials'])/all_stats['Tutorials']
        prop['Only hands-on'] = all_stats['Hands-on']/all_stats['Tutorials'] - prop['Both hands-on and slide deck']
        prop['Only slide deck'] = all_stats['Slide decks']/all_stats['Tutorials'] - prop['Both hands-on and slide deck']
        prop = prop * 100
        print(prop)


rule plot_technical_support:
    '''
    Plot number of topics, tutorials, etc
    '''
    input:
        repo_content_stats = "data/repo_content_stats"
    output:
        tech_support_stat_plot = "images/tech_support_stat_plot.png",
        tech_support_prop_plot = "images/tech_support_prop_plot.png"
    run:
        # load stats
        all_stats = pd.read_csv(str(input.repo_content_stats), index_col = 0)
        tech_support_stats = all_stats[["Tools", "Worflows", "Data on Zenodo", "Data for data libraries", "Interactive tours"]].transpose()
        # plot barplot stats
        fig = plt.plot()
        plt.subplot(2, 1, 1)
        ax = tech_support_stats.plot(kind='bar', legend=True, fontsize=12, color=["orange","darkblue"], title="Number in the repository")
        ax.set_xticklabels(tech_support_stats.index, rotation=45)
        plt.tight_layout()
        plt.savefig(str(output.tech_support_stat_plot), transparent=True)
        # extract proportions
        tech_support_perc = tech_support_stats
        tech_support_perc[[date]] = 100 * tech_support_perc[[date]]/all_stats.loc[date,"Hands-on"]
        tech_support_perc[["22.06.17"]] = 100 * tech_support_perc[["22.06.17"]]/all_stats.loc["22.06.17","Hands-on"]
        fig = plt.plot()
        ax = tech_support_perc.plot(kind='bar', legend = True, fontsize=12, color=["orange","darkblue"], title="Percentage of covered hands-on tutorials")
        ax.set_xticklabels(tech_support_perc.index, rotation=45)
        plt.tight_layout()
        plt.savefig(str(output.tech_support_prop_plot), transparent=True)

