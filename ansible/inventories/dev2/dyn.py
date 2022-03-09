#!/usr/bin/python
import json
import sys
import os
pp= os.path.dirname( os.path.abspath(__file__) )
fname=pp+'/../../../terra/terraform.tfstate'
f=open(fname)
j=json.load(f)
#print j
#print sys.argv
#--host
h={}
dc1=[]
dc2=[]
dc3=[]
dc4=[]
dc5=[]
dc6=[]
dc7=[]
dc8=[]
for item in j['resources']:
    if item['type'] =='digitalocean_droplet':
        name=item['instances'][0]['attributes']['name']
        ip=item['instances'][0]['attributes']['ipv4_address'] 
        if name.startswith('kafka'):
            dc1.append (ip)
            h[name]={"ansible_host":  ip , 
                     "ansible_user": "root",   
                      "dc_name": "dc1",
                       "ansible_ssh_common_args": "-o \"UserKnownHostsFile /dev/null\"",
                       "ansible_consul_group": "kafka"   }
        if name.startswith('zxbot'):
            dc5.append (ip)
            h[name]={"ansible_host":  ip , 
                     "ansible_user": "root",   
                      "dc_name": "dc8",
                       "ansible_ssh_common_args": "-o \"UserKnownHostsFile /dev/null\"",
                       "ansible_consul_group": "zxbot"   }

        if name.startswith('devops'):
            dc5.append (ip)
            h[name]={"ansible_host":  ip , 
                     "ansible_user": "root",   
                      "dc_name": "dc8",
                       "ansible_ssh_common_args": "-o \"UserKnownHostsFile /dev/null\"",
                       "ansible_consul_group": "devops"   }


        if name.startswith('docker'):
            dc5.append (ip)
            h[name]={"ansible_host":  ip , 
                     "ansible_user": "root",   
                      "dc_name": "dc1",
                       "ansible_ssh_common_args": "-o \"UserKnownHostsFile /dev/null\"",
                       "ansible_consul_group": "docker"   }
        if name.startswith('openshift'):
            dc6.append (ip)
            h[name]={"ansible_host":  ip , 
                     "ansible_user": "root",   
                      "dc_name": "dc1",
                       "ansible_ssh_common_args": "-o \"UserKnownHostsFile /dev/null\"",
                       "ansible_consul_group": "docker"   }


        if name.startswith('flink'):
            dc2.append(ip)
            h[name]={"ansible_host":  ip , 
                     "ansible_user": "root",   
                      "dc_name": "dc2",
                       "ansible_ssh_common_args": "-o \"UserKnownHostsFile /dev/null\"",
                       "ansible_consul_group": "flink"   }
        if name.startswith('click'):
            dc3.append(ip)
            h[name]={"ansible_host":  ip , 
                     "ansible_user": "root",   
                      "dc_name": "dc3",
                       "ansible_ssh_common_args": "-o \"UserKnownHostsFile /dev/null\"",
                       "ansible_consul_group": "click"   }
        if name.startswith('consul-dc1'):
            dc4.append(ip)
            h[name]={"ansible_host":  ip , 
                     "ansible_user": "root",   
                      "dc_name": "dc1",
                       "ansible_ssh_common_args": "-o \"UserKnownHostsFile /dev/null\"",
                       "ansible_consul_group": "consul-dc1"   }

        if name.startswith('consul-dc2'):
            dc7.append(ip)
            h[name]={"ansible_host":  ip , 
                     "ansible_user": "root",   
                      "dc_name": "dc2",
                       "ansible_ssh_common_args": "-o \"UserKnownHostsFile /dev/null\"",
                       "ansible_consul_group": "consul-dc2"   }


a={'_meta': {'hostvars': h} }
a['all'] = {  "children":["kafka","flink","click","consul-dc1","consul-dc2","openshift"] }
a['kafka']={'hosts':dc1}
a['flink']={'hosts':dc2}
a['click']={'hosts':dc3}
a['consul-dc1']={'hosts':dc4}
a['consul-dc2']={'hosts':dc7}
a['zxbot']={'hosts':dc8 }
a['devops']={'hosts':dc8 }
a['docker']={'hosts':dc5}
a['openshift']={'hosts':dc6}
if sys.argv[1]=='--list':
   print  json.dumps(a , indent=2)
if sys.argv[1]=='--host':
   host=sys.argv[2]
   print  json.dumps(h[host] , indent=2)
if sys.argv[1]=='--list2':
   h3=[]
   h3.extend(dc1)
   h3.extend(dc2)
   h3.extend(dc3)
   h3.extend(dc4)
   h3.extend(dc5)
   h3.extend(dc6)
   h3.extend(dc7)
   h3.extend(dc8)
   it=''
   for item in  h3:
     #print item, h3.index(item)
     if (h3.index(item)==0):
       it=item
     else:
       it=it+' '+item   
   print it

#./ec2.py --list
#"_meta": {
#        "hostvars": {
#            "dc1-consul-s1": {
#                "ansible_consul_group": "consul-dc1", 
#                "ansible_host": "178.62.237.225", 
#                "ansible_ssh_common_args": "-o \"UserKnownHostsFile /dev/null\"", 
#                "ansible_user": "root", 
#                "dc_name": "dc1"

