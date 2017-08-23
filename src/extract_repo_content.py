from github import Github
import base64
import yaml
from pprint import pprint


configfile: "config.yaml"

# connect to GitHub
g = Github(config["github"])
# retrieve the hub repository
hub_repo = g.get_user("galaxyproject").get_repo("training-material")


rule all:
    input:
        repo_content = "data/repo_content"


rule extract_repo_content:
    '''
    Extract the details about the current resources in the Galaxy Training Material
    '''
    output:
        repo_content = "data/repo_content"
    run:
        with open(str(output.repo_content), "w") as output:
            output.write('topic\ttarget\ttutorial\n')
            for file in hub_repo.get_dir_contents("metadata"):
                file_content = base64.b64decode(file.content)
                yaml_content = yaml.load(file_content)
                title = yaml_content['title']
                target = yaml_content['type']
                tutorials = []
                for tutorial in yaml_content['material']:
                    if tutorial['type'] == 'introduction':
                        continue
                    if 'enable' in tutorial and tutorial['enable'] == 'false':
                        continue
                    tutorials.append(tutorial['title'])
                output.write("%s\t%s\t%s\n" % (title, target, ', '.join(tutorials)))
