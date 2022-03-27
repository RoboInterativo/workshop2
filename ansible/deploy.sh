#!/bin/bash
ansible-playbook -vv -u root  -i   inventories/dev/inventory   $1 
#--tags $1
