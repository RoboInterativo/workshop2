#!/bin/bash
ansible-playbook -vv -u root --extra-vars "token=$TOKEN" -i   inventories/dev/inventory    playbooks/$1.yml 
#--tags $1
