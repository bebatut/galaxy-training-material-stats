from github import Github
import base64


configfile: "config.yaml"

# connect to GitHub
g = Github(config["github"])
# retrieve the hub repository
hub_repo = g.get_user("galaxyproject").get_repo("galaxy-hub")


def extract_details(file_content):
    """
    Extract resource details (format, type, domains) from the `index.md`
    """
    file_content = str(base64.b64decode(file_content))
    resource = file_content.find("Resource::")
    contact = file_content.find("Date::")
    content = file_content[resource:contact].split("\\n")

    resource = {'topics':[], 'formats':[], 'types':[], 'owners':[]}
    for line in content:
        line = line.rstrip()
        if line.find("Types") != -1:
            resource['types'] = line.split(":: ")[1].split(", ")
        elif line.find("Domains") != -1:
            resource['topics'] = line.split(":: ")[1].split("**")[1].split(", ")
        elif line.find("Formats") != -1:
            resource['formats'] = line.split(":: ")[1].split(", ")
        elif line.find("Owners") != -1:
            resource['owners'] = line.split(":: ")[1].replace("and",",").split(", ")
    for info in resource:
        for i in range(len(resource[info])):
            if resource[info][i].find("[") != -1:
                resource[info][i] = resource[info][i].split("[")[1].split("]")[0]
    return resource


rule all:
    input:
        previous_repo_content = "data/previous_repo_content"


rule extract_previous_teaching_resources:
    '''
    Extract the details about the previous resources in the GTN catalog
    '''
    output:
        previous_repo_content = "data/previous_repo_content"
    run:
        resource_nb = 0
        resources = {'topics':set(), 'formats':set(), 'types':set(), 'owners':set()}
        for content in hub_repo.get_dir_contents("src/teach/resource"):
            for file in hub_repo.get_dir_contents(content.path):
                if file.name != "index.md":
                    continue
                resource_nb += 1
                resource = extract_details(str(file.content))
                for res in resource:
                    resources[res] = resources[res].union(resource[res])
        for res in resource:
            resources[res] = list(resources[res])
            resources[res].sort()
        # Write the extracted information in a file
        with open(str(output.previous_repo_content), "w") as output:
            output.write("Number of resources\t%s\n" % (resource_nb))
            output.write("Topics\t%s\n" % (", ".join(resources['topics'])))
            output.write("Types\t%s\n" % (", ".join(resources['types'])))
            output.write("Formats\t%s\n" % (", ".join(resources['formats'])))
            output.write("Owners\t%s\n" % (", ".join(resources['owners'])))

