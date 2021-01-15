#!/usr/bin/python
import os
from cti.models import IP
from cti.models import Log_line
from cti.models import Apache_log

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


def saveIPs(uniqueIPs):
    for i in range(len(uniqueIPs)):
        ipFromFile = uniqueIPs[i]


        #if the ip is in the database, don't add it again
        if IP.objects.filter(address=ipFromFile).exists():
            continue
        

        details = getIPInfo(ipFromFile)

        try:
            hostname = details.hostname
        except:
            hostname = None
        try:
            city = details.city
        except:
            city = None
        try:
            region = details.region
        except:
            region = None
        try:
            country = details.country
        except:
            country = None
        try:
            countryname = details.country_name
        except:
            countryname = None
        try:
            org = details.org
        except:
            org = None
        try:
            postal = details.postal
        except:
            postal = None
        try:
            timezone = details.timezone
        except:
            timezone = None
        try:
            latitude = details.latitude
        except:
            latitude = None
        try:
            longitude = details.longitude
        except:
            longitude = None
        tempIP = IP(address = ipFromFile, hostname = hostname, city = city, region = region, country = country, countryname = countryname, org = org, postal = postal, timezone = timezone, latitude = latitude, longitude = longitude)
        tempIP.save()

def analyze(filename):
    print("filename1: " + str(filename))

    os.system('pwd')
    filenameString = str(filename)
    path = 'media/' + filenameString

    lines = []
    with open(path, 'r') as f: 
        lines = f.readlines()
        f.close()

    for i in range(len(lines)):  # strip newline char
        lines[i] = lines[i].rstrip()

    uniqueIPs = []
    uniqueIPs = IPFilter(lines)
    saveIPs(uniqueIPs)

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
        temp_log_line = Log_line( ip_address = IP.objects.get(address = ip_address),
                 timestamp = timestamp,
                 requestMethod = requestMethod,
                 path = path,
                 httpVersion = httpVersion,
                 response = response,
                 sizeInBytes = sizeInBytes)
        temp_log_line.save()

        print("filename2 " + str(filenameString))
        file = Apache_log.objects.get(log_file=filenameString) 
        file.analyzed = True
        file.save()


if __name__ == "__main__":
    main()


