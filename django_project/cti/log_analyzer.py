#!/usr/bin/python
import os
from cti.models import IP
from cti.models import Log_line
from cti.neo4j.neo4j_classes import create_node, get_nodes, create_relationship
import ipinfo 
access_token = '249b72c836625c'


def IPFilter(lines):
    uniqueIPs = []
    for i in range(len(lines)):
        if lines[i].split()[0] not in uniqueIPs:
            uniqueIPs.append(lines[i].split()[0])
    return uniqueIPs


def getIPInfo(ip_address):
    global access_token
    handler = ipinfo.getHandler(access_token)
    details = handler.getDetails(ip_address)
    return details


def saveIPs(uniqueIPs, server_data):
    for i in range(len(uniqueIPs)):
        ipFromFile = uniqueIPs[i]
        details = getIPInfo(ipFromFile)

        ip_attributes = {}
        ip_attributes['ip_address'] = ipFromFile

        try:
            ip_attributes['hostname'] = details.hostname
        except:
            hostname = None
        try:
            ip_attributes['city'] = details.city
        except:
            city = None
        try:
            ip_attributes['region'] = details.region
        except:
            region = None
        try:
            ip_attributes['country'] = details.country
        except:
            country = None
        try:
            ip_attributes['countryname'] = details.countryname
        except:
            countryname = None
        try:
            ip_attributes['org'] = details.org
        except:
            org = None
        try:
            ip_attributes['postal'] = details.postal
        except:
            postal = None
        try:
            ip_attributes['timezone'] = details.timezone
        except:
            timezone = None
        try:
            ip_attributes['latitude'] = details.latitude
        except:
            latitude = None
        try:
            ip_attributes['longitude'] = details.longitude
        except:
            longitude = None
        create_node('IP', ip_attributes)
        create_node('Server', server_data)
        create_relationship('IP', ip_attributes, 'Server', server_data, 'HAS_ACCESSED')

        return ip_attributes


def analyze(filename, server_data):
    os.system('pwd')
    filename = str(filename)
    path = 'media/' + filename

    lines = []
    with open(path, 'r') as f: 
        lines = f.readlines()
        f.close()

    for i in range(len(lines)):  # strip newline char
        lines[i] = lines[i].rstrip()

    uniqueIPs = []
    uniqueIPs = IPFilter(lines)
    ip_attributes = saveIPs(uniqueIPs, server_data)

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

        log_attributes = {
            "timestamp": timestamp,
            "requestMethod": requestMethod,
            "path": path,
            "httpVersion": httpVersion,
            "response": response,
            "sizeInBytes": sizeInBytes
        }

        create_node('Log_line', log_attributes)
        create_relationship('IP', ip_attributes, 'Log_line', log_attributes, 'HAS_SENT')

        # temp_log_line = Log_line( ip_address = IP.objects.get(address = ip_address),
        #          timestamp = timestamp,
        #          requestMethod = requestMethod,
        #          path = path,
        #          httpVersion = httpVersion,
        #          response = response,
        #          sizeInBytes = sizeInBytes)
        # temp_log_line.save()


if __name__ == "__main__":
    main()


