from .neo4j_db import Database

#metoda stvara novi cvor u bazi tipa class_name
# koji ima sve atribute zadane dictionaryjem attributes
#stvara cvor 'class_name' sa atributima 'attributes'
#class_name je string, a attributes je dictionary
def create_node(class_name, attributes):
    i = 0
    query_string = 'CREATE(label' + ':' + class_name + '{'
    for attribute in attributes:
        if i == 0:
            query_string += attribute + ': "' + attributes[attribute] + '"'
        else:
            query_string += ', ' + attribute + ': "' + attributes[attribute] + '"'
        i += 1
    query_string += '}) RETURN label'

    db = Database("bolt://localhost:7687", "neo4j", "password")
    return db.query(query_string)


#creates a node only if the node with the same name and exact same attributes doesn't already exist
# if it exists, that node is returned
#e.g. MERGE (charlie { name: 'Charlie Sheen', age: 10 }) RETURN charlie
def create_if_not_exist(class_name, attributes):
    i = 0
    query_string = 'MERGE(label' + ':' + class_name + '{'
    for attribute in attributes:
        if i == 0:
            query_string += attribute + ': "' + attributes[attribute] + '"'
        else:
            query_string += ', ' + attribute + ': "' + attributes[attribute] + '"'
        i += 1
    query_string += '}) RETURN label'

    db = Database("bolt://localhost:7687", "neo4j", "password")
    return db.query(query_string)

# creates a relationship between first_node_name and second_node_name only if it doesn't already exist
# if a relationship between nodes with properties first_node and second_node exists nothing happens
# ALL properties have to match for the database to realise it is a duplicate
def create_relationship_if_not_exist(first_node_name, first_node, second_node_name, second_node, relationship_name):
    i = 0
    j = 0
    query_string = 'MATCH(a:' + first_node_name + '),(b:' + second_node_name + ') WHERE '
    for attribute in first_node:
        if i == 0:
            query_string += 'a.' + attribute + ' = "' + first_node[attribute] + '"'
        else:
            query_string += ' AND a.' + attribute + ' = "' + first_node[attribute] + '"'
        i += 1
    for attribute in second_node:
        if j == 0:
            if i > 0:
                query_string += ' AND '
            query_string += 'b.' + attribute + ' = "' + second_node[attribute] + '"'
        else:
            query_string += ' AND b.' + attribute + ' = "' + second_node[attribute] + '"'
        j += 1
    query_string += ' MERGE(a)-[r:' + relationship_name + ']->(b) RETURN r'

    db = Database("bolt://localhost:7687", "neo4j", "password")
    return db.query(query_string)


#metoda stvara vezu između čvorova tipa first_node_name i second_node_name
# metoda prvou bazi traži čvorove tih tipova sa atributima zadanim s first_node i second_node
# ako takvih nema, baca izniku????
#first_node and second_node are dictionaries
#first_node_name, second_node_name and relationship_name are strings
def create_relationship(first_node_name, first_node, second_node_name, second_node, relationship_name):
    i = 0
    j = 0
    query_string = 'MATCH(a:' + first_node_name + '),(b:' + second_node_name + ') WHERE '
    for attribute in first_node:
        if i == 0:
            query_string += 'a.' + attribute + ' = "' + first_node[attribute] + '"'
        else:
            query_string += ' AND a.' + attribute + ' = "' + first_node[attribute] + '"'
        i += 1
    for attribute in second_node:
        if j == 0:
            if i > 0:
                query_string += ' AND '
            query_string += 'b.' + attribute + ' = "' + second_node[attribute] + '"'
        else:
            query_string += ' AND b.' + attribute + ' = "' + second_node[attribute] + '"'
        j += 1
    query_string += ' CREATE(a)-[r:' + relationship_name + ']->(b) RETURN r'

    db = Database("bolt://localhost:7687", "neo4j", "password")
    return db.query(query_string)


#metoda vraća sve čvorove tipa class_name s atributima zadanim u attributes
#klasa je ime čvora, parametri je dictionary sa where parametrima
def get_nodes(class_name, attributes):
    i = 0
    query_string = 'MATCH(label:' + class_name + '{'
    for attribute in attributes:
        if i == 0:
            query_string += attribute + ': "' + attributes[attribute] + '"'
        else:
            query_string += ', ' + attribute + ': "' + attributes[attribute] + '"'
        i += 1
    query_string += '}) RETURN label'

    db = Database("bolt://localhost:7687", "neo4j", "password")
    result = []
    for res in db.query(query_string):
        result.append(res['label'])
    return result
#example
#mydict = {
#    "datetime": "30/Aug/2020:03:24:31",
#        "method": "GET"
#}
#print(test('Request', mydict))

#vraća sve čvorove koji su u bazi
def get_all():
    query_string = 'MATCH (a) RETURN (a)'
    db = Database("bolt://localhost:7687", "neo4j", "password")
    return db.query(query_string)

#returns a list of properties on the node
#known_properties is a dictionary of at least one node property
#e.g. MATCH (a) WHERE a.name = '' RETURN keys(a)
def get_attributes(known_properties):
    i = 0
    query_string = 'MATCH(a) WHERE a.'
    for known_property in known_properties:
        if i == 0:
            query_string += known_property + ' = "' + known_properties[known_property] + '"'
        else:
            query_string += ' AND a.' + known_property + ' = "' + known_properties[known_property] + '"'
    query_string += 'RETURN keys(a)'

    db = Database("bolt://localhost:7687", "neo4j", "password")
    result = db.query(query_string)
    return result[0]['keys(a)']


# metoda vraća sve requestove koje je poslala ip adresa
def get_requests_for_ip(ip_address):
    query_string = 'MATCH(a:IP {ip_address: "' + ip_address + '"})-[:HAS_SENT]->(b:Log_line) RETURN b'
    db = Database("bolt://localhost:7687", "neo4j", "password")
    return db.query(query_string)

# metoda vraća sve jedinstvene ip adrese koje postoje u bazi
def get_count_of_ip():
    query_string = 'MATCH (p:IP) WITH DISTINCT p.ip_address as p RETURN count(p) as count'
    db = Database("bolt://localhost:7687", "neo4j", "password")
    ip_count = db.query(query_string)[0]['count']
    return ip_count

#metoda koja vraća listu 10 mapa ključ-country, vrijednost- broj sa najvećim brojem ip adresa
def get_Top_countries_by_ip():
    countries_dict = {}
    query_string = 'MATCH (n:IP) return DISTINCT n'
    db = Database("bolt://localhost:7687", "neo4j", "password")
    query_result = db.query(query_string)
    for ip in query_result:
        country = ip['n']['country']
        if country in countries_dict.keys():
            countries_dict[country] += 1
        else :
            countries_dict[country] = 1
    countries_dict_sorted = sorted(countries_dict.items(), key=lambda x: x[1], reverse=True)
    countries_dict_sorted_view = []
    if len(countries_dict_sorted)<10:
        range_of_countries = len(countries_dict_sorted)
    else :
        range_of_countries = 10
    for i in range (range_of_countries):
        help_dict = {}
        help_dict['country'] = countries_dict_sorted[i][0]
        help_dict['c'] = countries_dict_sorted[i][1]
        countries_dict_sorted_view.append(help_dict)
    return countries_dict_sorted_view

#metoda za search po ip adresi
def get_by_ip(ip_address):
    query_string = 'MATCH (n) WHERE n.ip_address="' + ip_address+ '" RETURN n '
    db = Database("bolt://localhost:7687", "neo4j", "password")
    response = db.query(query_string)
    response_list = []
    for i in response:
        response_list.append(i['n'])
    return response_list

#metoda za search po country code
def get_by_country_code(countryCode):
    query_string = 'MATCH (n) WHERE n.country="' + countryCode + '" RETURN n '
    db = Database("bolt://localhost:7687", "neo4j", "password")
    response = db.query(query_string)
    response_list = []
    for i in response:
        response_list.append(i['n'])
    return response_list

#metoda za search po country name - toga više nema!!
# def get_by_country_name(countryName):
#     query_string = 'MATCH (n) WHERE n.countryname="' + countryName + '" RETURN n '
#     db = Database("bolt://localhost:7687", "neo4j", "password")
#     response = db.query(query_string)
#     response_list = []
#     for i in response:
#         response_list.append(i['n'])
#     return response_list   

#metoda za search po city
def get_by_city(city):
    query_string = 'MATCH (n) WHERE n.city="' + city + '" RETURN n '
    db = Database("bolt://localhost:7687", "neo4j", "password")
    response = db.query(query_string)
    response_list = []
    for i in response:
        response_list.append(i['n'])
    return response_list   

#metoda za search po region
def get_by_region(region):
    query_string = 'MATCH (n) WHERE n.region="' + region + '" RETURN n '
    db = Database("bolt://localhost:7687", "neo4j", "password")
    response = db.query(query_string)
    response_list = []
    for i in response:
        response_list.append(i['n'])
    return response_list  

#metoda za search po org
def get_by_org(org):
    query_string = 'MATCH (n) WHERE n.org="' + org + '" RETURN n '
    db = Database("bolt://localhost:7687", "neo4j", "password")
    response = db.query(query_string)
    response_list = []
    for i in response:
        response_list.append(i['n'])
    return response_list  

#metoda za search po postal
def get_by_postal(postal):
    query_string = 'MATCH (n) WHERE n.postal="' + str(postal) + '" RETURN n '
    db = Database("bolt://localhost:7687", "neo4j", "password")
    response = db.query(query_string)
    response_list = []
    for i in response:
        response_list.append(i['n'])
    return response_list  

#metoda za search po timezone
def get_by_timezone(timezone):
    query_string = 'MATCH (n) WHERE n.timezone="' + timezone + '" RETURN n '
    db = Database("bolt://localhost:7687", "neo4j", "password")
    response = db.query(query_string)
    response_list = []
    for i in response:
        response_list.append(i['n'])
    return response_list  

# returns all IP addresses that have sent a request with the requestMethod = request_method
# (request_method is a string e.g. 'GET')
# MATCH(a:IP)-[:HAS_SENT]->(b:Log_line {requestMethod:'GET'}) return a
def get_ips_with_request_method(request_method):
    query_string = 'MATCH(a:IP)-[:HAS_SENT]->(b:Log_line {requestMethod: "' + request_method + '"}) RETURN DISTINCT a'
    db = Database("bolt://localhost:7687", "neo4j", "password")
    return db.query(query_string)
