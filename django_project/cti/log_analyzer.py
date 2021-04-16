#!/usr/bin/python
import os
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

        details = getIPInfo(ip_address)

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
        create_relationship_if_not_exist('IP', ip_attributes, 'Log_line', log_attributes, 'HAS_SENT')
        create_relationship_if_not_exist('Log_line', log_attributes, 'Server', server_data, 'HAS_ACCESSED')

        print("filename2 " + str(filenameString))
        file = Apache_log.objects.get(log_file=filenameString) 
        file.analyzed = True
        file.save()


if __name__ == "__main__":
    main()


