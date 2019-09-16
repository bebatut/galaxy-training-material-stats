- **Ansible**
  - Pro:
    - It's easy to follow. (*30/10/2018*)
    - excellent intro, thanks! (*02/11/2018*)
    - TEST (*15/11/2018*)
    - Examples and documentation are easy to follow (*01/07/2019*)
  - Con:
    - For clean Ubuntu 18.04 Ansible couldn't find python (it was not installed, weird), so it crashed. There should be rule added to check and install python if it is not installed. Refer to this solution - https://gist.github.com/gwillem/4ba393dceb55e5ae276a87300f6b8e6f. (*30/10/2018*)
    - TEST (*15/11/2018*)

- **Deploying a compute cluster in OpenStack via Terraform**
  - Pro:
    - Really detailed, could use it for my project for creating my project (*19/12/2018*)
  - Con:
    - maybe go deeper and show a template for a project (*19/12/2018*)

- **Galaxy Installation on Kubernetes**


- **Galaxy Installation with Ansible**
  - Pro:
    - examples (*28/01/2019*)
    - This is wonderful tutorial and love to attend this training next time (*22/03/2019*)
    - well explained :) (*01/07/2019*)
    - Very good step by step procedure. (*01/07/2019*)
    - I already followed this tutorial by my own before GCC. (*01/07/2019*)
    - extremely well done - thank you training material authors and presenters (*01/07/2019*)
    - Most everything could be copied and pasted into a running VM. (*01/07/2019*)
    - The step by step approach and the numerous examples to do a quick copy. In this way one can focus on the concepts and leave the hard (also boring) work of writing correct yaml files behind. (*01/07/2019*)
  - Con:
    - solution for proftp (*28/01/2019*)
    - Yes, I'm having problem with the configuration of the certbot certificate for the production environment. With cluster connection (*22/03/2019*)
    - sometimes it is not clear in the exercises which files have to be edited, or the code is not ready to copy-paste, which leads to misunderstandings.  I would love to see the whole explanation of the variables of the config files you did (specially nginx) written down to check them when needed. (*01/07/2019*)
    - perhaps more emphasis on some steps (geerlingguy.pip during supervisord) (*01/07/2019*)
    - I would add all the galaxy.yml and modify it instead of copy/paste some element in the playbook. For me, it's easier to get update shiped with each Galaxy update. (*01/07/2019*)
    - 1) ssh connection timeout is too short, disconnects while running playbooks. (2) sometimes the insertion point for yaml section in the exercices could be more explicit (*01/07/2019*)
    - The working playbook could be presented in its own git repo (or whatever) with tags after each step, so that the user can diff two tags to see what changed in the next step.  I made a shar file of the completed playbook, but I didn't think to init a git repo and commit/tag after each step started working. (*01/07/2019*)
    - I think that some users have felt overwhelmed by trying to learn Ansible so quickly. It would be better if the guidelines suggested that a basic knowledge of Ansible is required in order to follow this training proficiently. Maybe a link,  before the training, to some material on Ansible  would be helpful as well. (*01/07/2019*)

- **Galaxy Tool Management**


- **Managing Galaxy on Kubernetes**
  - Pro:
    - this was way super cool (*03/07/2019*)
  - Con:
    - maybe specify that the parts in Setting admin... part 1 should go under the galaxy: heading for those not as familiar with galaxy configs? or can we assume they're all savvy? templates/deployment_web.yaml -> dash, not underscore (*03/07/2019*)

- **Reference Data with CVMFS**

  - Con:
    - the samples are great and its great to have the copy capacity, but some of those copies could mess people up (ones with ..., snippets of yaml that start with ---, etc) (*04/07/2019*)

- **Running Jobs on Remote Resources with Pulsar**
  - Pro:
    - nothing! (*02/05/2019*)
  - Con:
    - everything; I recommend you go through it entirely and minimize the amount of "assumed" knowledge; after 6h I still don't have pulsar running, and I quit. For instance, it took a while to understand there is no default "working directory", you just mean "any" folder in this sentence: "From your ansible working directory, edit the requirements.yml file and add the following line:" Also, it took me a very long time to figure out that on a fresh VM, there is no "requirements.yml" file! I need to create it.   (*02/05/2019*)

