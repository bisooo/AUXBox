# AUXBox
## Version: 1.0

## Installation 

### Requirements
-  Ansible
-  A database
-  Linux Server
-  Valid ssh key configuration to server

### Steps
-  Open vars.yml
-  Add the variables related to the application
-  Open inventory/hosts.yml
-  Add the host specific information

### Build Command
>> ansible-playbook main.yml -i inventory/
