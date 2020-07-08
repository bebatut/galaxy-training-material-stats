- **Ansible**
  - Pro:
    - It's easy to follow. (*2018-10-30 00:00:00*)
    - excellent intro, thanks! (*2018-11-02 00:00:00*)
    - TEST (*2018-11-15 00:00:00*)
    - Examples and documentation are easy to follow (*2019-07-01 00:00:00*)
    - Formatting  (*2019-12-18 00:00:00*)
    - Step-by-Step guide, simple and well informative (*2020-02-14 00:00:00*)
    - All of it (*2020-03-02 00:00:00*)
    - hands on exercises (*2020-05-08 00:00:00*)
  - Con:
    - For clean Ubuntu 18.04 Ansible couldn't find python (it was not installed, weird), so it crashed. There should be rule added to check and install python if it is not installed. Refer to this solution - https://gist.github.com/gwillem/4ba393dceb55e5ae276a87300f6b8e6f. (*2018-10-30 00:00:00*)
    - TEST (*2018-11-15 00:00:00*)
    - Methods and examples of overriding or changing settings of galaxy roles that are hidden in the .ansible folder (*2019-12-18 00:00:00*)
    - Looks very good, with basic sample tasks. (*2020-03-02 00:00:00*)

- **Automation with Jenkins**


- **Deploying a compute cluster in OpenStack via Terraform**
  - Pro:
    - Really detailed, could use it for my project for creating my project (*2018-12-19 00:00:00*)
    - detailed explanations and working examples (*2019-11-20 00:00:00*)
    - Very clear step by step instructions (*2020-05-08 00:00:00*)
    - Basically I love all of them, It's simple, clear and easy to follow. (*2020-06-20 00:00:00*)
  - Con:
    - maybe go deeper and show a template for a project (*2018-12-19 00:00:00*)
    - showing how to attach volumes to the exec vm's (ie, create n volumes, and connect one to each vm to use for that vm's state / docker volume) (*2019-11-20 00:00:00*)
    - Some  examples can be added for networking and storage / filesystem addiotion. (*2020-05-08 00:00:00*)
    - Would be nice to have more complex examples to follow, if that possible (*2020-06-20 00:00:00*)

- **Ephemeris for Galaxy Tool Management**
  - Pro:
    - best practices description (*2020-03-03 00:00:00*)
  - Con:
    - please remove $ from solution commands (*2020-03-03 00:00:00*)

- **External Authentication**


- **Galaxy Installation on Kubernetes**


- **Galaxy Installation with Ansible**
  - Pro:
    - examples (*2019-01-28 00:00:00*)
    - This is wonderful tutorial and love to attend this training next time (*2019-03-22 00:00:00*)
    - well explained :) (*2019-07-01 00:00:00*)
    - Very good step by step procedure. (*2019-07-01 00:00:00*)
    - I already followed this tutorial by my own before GCC. (*2019-07-01 00:00:00*)
    - extremely well done - thank you training material authors and presenters (*2019-07-01 00:00:00*)
    - Most everything could be copied and pasted into a running VM. (*2019-07-01 00:00:00*)
    - The step by step approach and the numerous examples to do a quick copy. In this way one can focus on the concepts and leave the hard (also boring) work of writing correct yaml files behind. (*2019-07-01 00:00:00*)
    - Everthing (*2020-02-14 00:00:00*)
    - exhaustive (*2020-03-02 00:00:00*)
    - Following the tutorial is pretty straightforward (*2020-03-02 00:00:00*)
    - Tutorial includes code steps very clearly. (*2020-05-05 00:00:00*)
  - Con:
    - solution for proftp (*2019-01-28 00:00:00*)
    - Yes, I'm having problem with the configuration of the certbot certificate for the production environment. With cluster connection (*2019-03-22 00:00:00*)
    - sometimes it is not clear in the exercises which files have to be edited, or the code is not ready to copy-paste, which leads to misunderstandings.  I would love to see the whole explanation of the variables of the config files you did (specially nginx) written down to check them when needed. (*2019-07-01 00:00:00*)
    - perhaps more emphasis on some steps (geerlingguy.pip during supervisord) (*2019-07-01 00:00:00*)
    - I would add all the galaxy.yml and modify it instead of copy/paste some element in the playbook. For me, it's easier to get update shiped with each Galaxy update. (*2019-07-01 00:00:00*)
    - 1) ssh connection timeout is too short, disconnects while running playbooks. (2) sometimes the insertion point for yaml section in the exercices could be more explicit (*2019-07-01 00:00:00*)
    - The working playbook could be presented in its own git repo (or whatever) with tags after each step, so that the user can diff two tags to see what changed in the next step.  I made a shar file of the completed playbook, but I didn't think to init a git repo and commit/tag after each step started working. (*2019-07-01 00:00:00*)
    - I think that some users have felt overwhelmed by trying to learn Ansible so quickly. It would be better if the guidelines suggested that a basic knowledge of Ansible is required in order to follow this training proficiently. Maybe a link,  before the training, to some material on Ansible  would be helpful as well. (*2019-07-01 00:00:00*)
    - it would be nice to go a bit slower during the Galaxy installation, it was quite quick ! (*2020-03-02 00:00:00*)
    - It would be interesting to have a big picture of the processes / config files. Literally a big picture about which parts are we configuring and what are the implications. (*2020-03-02 00:00:00*)
    - This is focused for paid distros.  Centos 7/8 builds do not work due to package requirements and availability (*2020-05-05 00:00:00*)
    - The difference between galaxy_server_dir and galaxy_root is unclear. Should they be nested? Which of these is needed in a shared file-system? Maybe provide best-practice values for both, so it becomes more clear how they interact with each other. (*2020-05-08 00:00:00*)
    - In the section "Galaxy" we add uchida.miniconda which has to run as galaxy user and a few linse above is explained that a new user is created without sudo privileges for security reasons. The execution of uchida.miniconda with become: true and become_user: galaxy will fail, because this role requires sudo. I tried to install the dependencies tar and bzip2 in my playbook beforehand, but the role still requires sudo to check if the packages are installed. When i install the package with a root-user, it is possible to execute the /tmp/Miniconda...sh file with the galaxy user. Not sure if other stuff works in miniconda too. Why does this role need to be executed as galaxy user? This is somewhat unclear and leads to an installation-error. (*2020-07-06 00:00:00*)
    - In the nginx-part, the template needs an update to reflect 20.05 changes. The folder /blue doesnt exist anymore, its just "alias {{ galaxy_server_dir }}/static/style"      # The style directory is in a slightly different location     location /static/style {         alias {{ galaxy_server_dir }}/static/style/blue;         expires 24h;     } (*2020-07-07 00:00:00*)

- **Galaxy Monitoring with Reports**
  - Pro:
    - Thanks to ansible, easy to install :) (*2020-03-04 00:00:00*)

- **Galaxy Monitoring with Telegraf and Grafana**


- **Galaxy Monitoring with gxadmin**
  - Pro:
    - query implementation (*2020-03-04 00:00:00*)
  - Con:
    - @bgruening’s favourite: gxamdin query latest-users spelling issue gxadmin not working (*2020-03-04 00:00:00*)

- **Galaxy Tool Management**


- **Managing Galaxy on Kubernetes**
  - Pro:
    - this was way super cool (*2019-07-03 00:00:00*)
  - Con:
    - maybe specify that the parts in Setting admin... part 1 should go under the galaxy: heading for those not as familiar with galaxy configs? or can we assume they're all savvy? templates/deployment_web.yaml -> dash, not underscore (*2019-07-03 00:00:00*)

- **Reference Data with CVMFS**

  - Con:
    - the samples are great and its great to have the copy capacity, but some of those copies could mess people up (ones with ..., snippets of yaml that start with ---, etc) (*2019-07-04 00:00:00*)

- **Running Jobs on Remote Resources with Pulsar**
  - Pro:
    - nothing! (*2019-05-02 00:00:00*)
    - Very comprehensive tutorial. Helped me a lot (*2020-03-04 00:00:00*)
    - Content (*2020-03-04 00:00:00*)
    - I like testing pulsar section allow me to see changes and how things works  (*2020-03-04 00:00:00*)
  - Con:
    - everything; I recommend you go through it entirely and minimize the amount of "assumed" knowledge; after 6h I still don't have pulsar running, and I quit. For instance, it took a while to understand there is no default "working directory", you just mean "any" folder in this sentence: "From your ansible working directory, edit the requirements.yml file and add the following line:" Also, it took me a very long time to figure out that on a fresh VM, there is no "requirements.yml" file! I need to create it.   (*2019-05-02 00:00:00*)
    - Maybe still take it slow when editing the various files. It's sometimes hard to follow with the numerous kind of configuration files. (*2020-03-04 00:00:00*)
    - Hint can be added : pulsar.managers.queued_drmaa manager module could not be loaded: Could not find drmaa library.  Please specify its full path using the environment variable DRMAA_LIBRARY_PATH   It means ansible-playbook galaxy.yml wasn't re-run (*2020-03-04 00:00:00*)

