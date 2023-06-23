#!/usr/bin/env python
import requests
import os
import json
import yaml
from yaml.loader import SafeLoader
import sys


def get_project (TOKEN):
    # api-endpoint
    URL = "https://api.clo.ru/v1/projects"

    # defining a dict of headers to be sent to the API
    HEADERS = {'Content-Type': 'application/json', 'Authorization': f'Bearer {TOKEN}'}

    # sending get request and saving the response as response object
    r = requests.get(url = URL, headers = HEADERS)
    project_id=(r.json()['results'][0]['id'])
    return project_id

def get_servers (TOKEN,project_id):

    URL = f"https://api.clo.ru/v1/projects/{project_id}/servers"
    HEADERS = {'Content-Type': 'application/json', 'Authorization': f'Bearer {TOKEN}'}
    #
    # # defining a dict of headers to be sent to the API
    # HEADERS = {'Content-Type': 'application/json', 'Authorization': 'Bearer b7d03a6947b217efb6f3ec3bd3504582'}
    #
    # # sending get request and saving the response as response object
    r = requests.get(url = URL, headers = HEADERS)
    return  r.json ()

def get_image (TOKEN,project_id):

    URL = f"https://api.clo.ru/v1/projects/{project_id}/images"
    HEADERS = {'Content-Type': 'application/json', 'Authorization': f'Bearer {TOKEN}'}
    r = requests.get(url = URL, headers = HEADERS)
    return r.json()

def get_image_by_name (TOKEN,project_id,name):
    results=get_image (TOKEN,project_id)['results']
    rez=None
    for item in results:
        if (item['name']==name):
            rez=item
    return rez['id']

def create_server(TOKEN,project_id,params):
    # api-endpoint
    URL = f"https://api.clo.ru/v1/projects/{project_id}/servers"
    HEADERS = {'Content-Type': 'application/json', 'Authorization': f'Bearer {TOKEN}'}

    image_id=get_image_by_name (TOKEN,project_id,params['image_name'])
    keypairs=get_keypairs(TOKEN,project_id)
    keys=[]
    print (keypairs)
    for item in keypairs:
        keys.append( item['id'])
    # sending get request and saving the response as response object
    data = {
        "name": params['name'],
        "flavor": {
            "ram": params['ram'],
            "vcpus": params['cpu']
        },
        "image": image_id,
        "addresses": [

            {"version": 4, "external": False, "with_floating": True},
        ],
        'keypairs': keys,
        "storages": [
            {
                "size": params['disk'],
                "bootable": True,
                "storage_type": "volume"
            }

        ]
    }
    print (data)
    r = requests.post(        url = URL,json=data,        headers = HEADERS        )

    print (r.text)

def get_keypairs (TOKEN,project_id):
    URL = "https://api.clo.ru/v1/keypairs"
    HEADERS = {'Content-Type': 'application/json', 'Authorization': f'Bearer {TOKEN}'}
    r = requests.get(url = URL, headers = HEADERS)
    return r.json()['results']

def delete_server (TOKEN,project_id,id):
    # api-endpoint
    URL = f"https://api.clo.ru/v1/servers/{id}"

    # defining a dict of headers to be sent to the API
    HEADERS = {'Content-Type': 'application/json', 'Authorization': f'Bearer {TOKEN}'}

    # sending get request and saving the response as response object
    r = requests.delete(url = URL, headers = HEADERS)

    return r
def get_netdisk (TOKEN,project_id):
    URL = f"https://api.clo.ru/v1/projects/{project_id}/volumes"

    # defining a dict of headers to be sent to the API
    HEADERS = {'Content-Type': 'application/json', 'Authorization': f'Bearer {TOKEN}'}

    # sending get request and saving the response as response object
    r = requests.get(url = URL, headers = HEADERS)
    j=r.json()
    return j
    # print (json.dumps(j))
def delete_netdisk (TOKEN,project_id,id):
    # api-endpoint
    URL = f"https://api.clo.ru/v1/volumes/{id}"

    # defining a dict of headers to be sent to the API
    HEADERS = {'Content-Type': 'application/json', 'Authorization': f'Bearer {TOKEN}'}

    # sending get request and saving the response as response object
    r = requests.delete(url = URL, headers = HEADERS)
    print (r.text)
    #return r.json()
def get_floatip (TOKEN,project_id):
    # api-endpoint
    URL = f"https://api.clo.ru/v1/projects/{project_id}/floatingips"

    # defining a dict of headers to be sent to the API
    HEADERS = {'Content-Type': 'application/json', 'Authorization': f'Bearer {TOKEN}'}
    r = requests.get(url = URL, headers = HEADERS)
    return r.json()

def delete_floating_ip (TOKEN,project_id,id):
    URL = f"https://api.clo.ru/v1/floatingips/{id}"
    HEADERS = {'Content-Type': 'application/json', 'Authorization': f'Bearer {TOKEN}'}


    # defining a dict of headers to be sent to the API

    # sending get request and saving the response as response object
    r = requests.delete(url = URL, headers = HEADERS)
    print (r.text)
def create (TOKEN,project_id,conf):
    for server in conf['servers']:
        create_server(TOKEN,project_id,server)


def destroy (TOKEN,project_id,conf):
    server_list=get_servers (TOKEN,project_id)['results']
    serv_dict={}
    for item in server_list:
        serv_dict[item['name']]=item['id']

    print (json.dumps(serv_dict))
    for server in conf['servers']:
        print (serv_dict)
        if server['name'] in serv_dict.keys():
            id=serv_dict[ server['name'] ]
            r=delete_server(TOKEN,project_id,id)
            # print (server['name'],id)
            # print (r.text)
    list_disks=get_netdisk (TOKEN,project_id)['results']
    print (list_disks)
    for item in list_disks:
        if item['attached_to_server'] is None:
            id=item['id']
            delete_netdisk (TOKEN,project_id,id)
    list_ip=get_floatip (TOKEN,project_id)['results']
    for item in list_ip:
        if item['status'] == "DOWN":
            id=item['id']
            delete_floating_ip (TOKEN,project_id,id)







if __name__ == '__main__':
    TOKEN = os.getenv('CLOTOKEN')
    project_id=get_project (TOKEN)
    yml = open('infra.yml', 'r')    # 'document.yaml' contains a single YAML document.
    conf = yaml.load(yml, Loader=SafeLoader)
    # print (conf)
    # print ("Number of arguments:", len(sys.argv), "arguments")
    # print ("Argument List:", str(sys.argv))
    if 'destroy' in sys.argv:
        destroy (TOKEN,project_id,conf)
    if 'listdisk' in sys.argv:
        j=get_netdisk (TOKEN,project_id)
        print (json.dumps(j))
    if 'listip' in sys.argv:
        j=get_floatip (TOKEN,project_id)
        print (json.dumps(j))
    if 'getkey' in sys.argv:
        j=get_keypairs (TOKEN,project_id)
        print (json.dumps(j))

    if 'create' in sys.argv:
        create (TOKEN,project_id,conf)



    # j=get_image_by_name (TOKEN,project_id,'Ubuntu 20')
    # print (json.dumps(j))
    # j=get_keypairs (TOKEN,project_id,)
    # print (json.dumps(j))
    # j=get_servers(TOKEN,project_id)
    # print (json.dumps(j))
