#!/usr/bin/python
import os
import pluggy
import requests
import json
from cti.models import IP
from cti.models import Log_line
from cti.models import Apache_log
from cti.neo4j.neo4j_classes import create_relationship_if_not_exist, create_node_if_not_exist

import ipinfo
access_token = '5a8dcf646a1d15'


def getIPInfo(ip_address):
    global access_token
    handler = ipinfo.getHandler(access_token)
    details = handler.getDetails(ip_address)
    return details


def getIpStack(ip_address):
    url = "http://api.ipstack.com/" + ip_address + \
        "?access_key=f80fa8b45951161b9a0148ab143ccce6"
    response = requests.request("GET", url)
    print(response.text)
    return details


hookspec = pluggy.HookspecMarker("cti")
hookimpl = pluggy.HookimplMarker("cti")


class MySpec:

    @hookspec
    def myhook(self, ip_address):
        """Hook.
        """


class Plugin_1:

    @hookimpl
    def myhook(self, ip_address):
        print("Using ipinfo plugin")
        global access_token
        handler = ipinfo.getHandler(access_token)
        details = handler.getDetails(ip_address)
        return details


class Plugin_2:

    @hookimpl
    def myhook(self, ip_address):
        print("Using ipstack plugin")
        url = "http://api.ipstack.com/" + ip_address + \
            "?access_key=f80fa8b45951161b9a0148ab143ccce6"
        response = requests.request("GET", url)
        parsed_json = (json.loads(response.text))
        details = {'ip_address': parsed_json['ip'],
           'hostname': 'No hostname',
           'city': parsed_json['city'],
           'region': parsed_json['region_name'],
           'country': parsed_json['country_code'],
           'countryname': parsed_json['country_name'],
           'org': 'No ORG',
           'postal': parsed_json['zip'],
           'timezone': 'No timezone',
           'latitude': parsed_json['latitude'],
           'longitude': parsed_json['longitude']
           }
        return details

class Plugin_3:

    @hookimpl
    def myhook(self, ip_address):
        print("Using freegeoip plugin")
        url = "https://freegeoip.app/json/"+ ip_address
        headers = {
            'accept': "application/json",
            'content-type': "application/json"
            }
        response = requests.request("GET", url, headers=headers)
        parsed_json = (json.loads(response.text))
        details = {'ip_address': parsed_json['ip'],
           'hostname': 'No hostname',
           'city': parsed_json['city'],
           'region': parsed_json['region_name'],
           'country': parsed_json['country_code'],
           'countryname': parsed_json['country_name'],
           'org': 'No ORG',
           'postal': parsed_json['zip_code'],
           'timezone': parsed_json['time_zone'],
           'latitude': parsed_json['latitude'],
           'longitude': parsed_json['longitude']
           }
        return details


# create a manager and add the spec
pm = pluggy.PluginManager("cti")
pm.add_hookspecs(MySpec)





def analyze(filename, server_data):

    os.system('pwd')
    filenameString = str(filename)
    path = 'media/' + filenameString

    lines = []
    with open(path, 'r') as f:
        lines = f.readlines()
        f.close()

    for i in range(len(lines)):  # strip newline char
        lines[i] = lines[i].rstrip()

    create_node_if_not_exist('Server', server_data)
    # register plugins - uncomment the one you want to use
    # pm.register(Plugin_1())
    # pm.register(Plugin_2())
    pm.register(Plugin_3())

    for i in range(len(lines)):
        line = lines[i]
        details = line.split()
        ip_address = details[0]
        timestamp = details[3][1:]
        requestMethod = details[5][1:]
        path = details[6]
        httpVersion = details[7][-4:-1]
        response = details[8]
        sizeInBytes = details[9]
        


        details = pm.hook.myhook(ip_address = details[0])

        ip_attributes = {}
        ip_attributes['ip_address'] = ip_address

        try:
            ip_attributes['hostname'] = details.hostname
        except:
            hostname = None  # if hostname isn't found for this IP address then ignore it
        try:
            ip_attributes['city'] = details.city
        except:
            city = None  # ignore
        try:
            ip_attributes['region'] = details.region
        except:
            region = None  # ignore
        try:
            ip_attributes['country'] = details.country
        except:
            country = None  # ignore
        try:
            ip_attributes['countryname'] = details.countryname
        except:
            countryname = None  # ignore
        try:
            ip_attributes['org'] = details.org
        except:
            org = None  # ignore
        try:
            ip_attributes['postal'] = details.postal
        except:
            postal = None  # ignore
        try:
            ip_attributes['timezone'] = details.timezone
        except:
            timezone = None  # ignore
        try:
            ip_attributes['latitude'] = details.latitude
        except:
            latitude = None  # ignore
        try:
            ip_attributes['longitude'] = details.longitude
        except:
            longitude = None  # ignore
        create_node_if_not_exist('IP', ip_attributes)

        log_attributes = {
            "timestamp": timestamp,
            "requestMethod": requestMethod,
            "path": path,
            "httpVersion": httpVersion,
            "response": response,
            "sizeInBytes": sizeInBytes
        }

        create_node_if_not_exist('Log_line', log_attributes)
        create_relationship_if_not_exist(
            'IP', ip_attributes, 'Log_line', log_attributes, 'HAS_SENT')
        create_relationship_if_not_exist(
            'Log_line', log_attributes, 'Server', server_data, 'HAS_ACCESSED')

        print("filename2 " + str(filenameString))
        file = Apache_log.objects.get(log_file=filenameString)
        file.analyzed = True
        file.save()


if __name__ == "__main__":
    main()
