from .neo4j_db import Database

db_url = 'bolt://localhost:7687'
db_name = 'neo4j'
db_password = 'password'


# creates a node of "type" node_label with properties specified in the dictionary node_properties
# node_label should be a string (with no spaces in between)
def create_node(node_label, node_properties):
    i = 0
    query_string = 'CREATE(label' + ':' + node_label + '{'
    for node_property in node_properties:
        if i == 0:
            query_string += node_property + ': "' + node_properties[node_property] + '"'
        else:
            query_string += ', ' + node_property + ': "' + node_properties[node_property] + '"'
        i += 1
    query_string += '}) RETURN label'

    db = Database(db_url, db_name, db_password)
    return db.query(query_string)


# creates a node of "type" node_label with properties specified in the dictionary node_properties
# but only if a node with the same label and exactly the same properties doesn't already exist
# if such a node exists the method returns it
# node_label should be a string (with no spaces in between), node_properties should be a dictionary
# e.g. MERGE (charlie { name: 'Charlie Sheen', age: 10 }) RETURN charlie
def create_node_if_not_exist(node_label, node_properties):
    i = 0
    query_string = 'MERGE(label' + ':' + node_label + '{'
    for node_property in node_properties:
        if i == 0:
            query_string += node_property + ': "' + node_properties[node_property] + '"'
        else:
            query_string += ', ' + node_property + ': "' + node_properties[node_property] + '"'
        i += 1
    query_string += '}) RETURN label'

    db = Database(db_url, db_name, db_password)
    return db.query(query_string)


# creates a relationship between a node of "type" first_node_label and a node of "type"second_node_label
# first_node_label, second_node_label and relationship_label should be strings (with no spaces)
# first_node_properties and second_node_properties should be dictionaries
def create_relationship(first_node_label, first_node_properties, second_node_label, second_node_properties, relationship_label):
    i = 0
    j = 0
    query_string = 'MATCH(a:' + first_node_label + '),(b:' + second_node_label + ') WHERE '
    for node_property in first_node_properties:
        if i == 0:
            query_string += 'a.' + node_property + ' = "' + first_node_properties[node_property] + '"'
        else:
            query_string += ' AND a.' + node_property + ' = "' + first_node_properties[node_property] + '"'
        i += 1
    for node_property in second_node_properties:
        if j == 0:
            if i > 0:
                query_string += ' AND '
            query_string += 'b.' + node_property + ' = "' + second_node_properties[node_property] + '"'
        else:
            query_string += ' AND b.' + node_property + ' = "' + second_node_properties[node_property] + '"'
        j += 1
    query_string += ' CREATE(a)-[r:' + relationship_label + ']->(b) RETURN r'

    db = Database(db_url, db_name, db_password)
    return db.query(query_string)


# creates a relationship between a node of "type" first_node_label and a node of "type"second_node_label
# but only if such a relationship (ALL node properties have to match) doesn't already exist
# if such a relationship already exists nothing happens in the database and the method returns the relationship
def create_relationship_if_not_exist(first_node_label, first_node_properties, second_node_label, second_node_properties, relationship_label):
    i = 0
    j = 0
    query_string = 'MATCH(a:' + first_node_label + '),(b:' + second_node_label + ') WHERE '
    for node_property in first_node_properties:
        if i == 0:
            query_string += 'a.' + node_property + ' = "' + first_node_properties[node_property] + '"'
        else:
            query_string += ' AND a.' + node_property + ' = "' + first_node_properties[node_property] + '"'
        i += 1
    for node_property in second_node_properties:
        if j == 0:
            if i > 0:
                query_string += ' AND '
            query_string += 'b.' + node_property + ' = "' + second_node_properties[node_property] + '"'
        else:
            query_string += ' AND b.' + node_property + ' = "' + second_node_properties[node_property] + '"'
        j += 1
    query_string += ' MERGE(a)-[r:' + relationship_label + ']->(b) RETURN r'

    db = Database(db_url, db_name, db_password)
    return db.query(query_string)


# returns all nodes of "type" node_label with properties specified in the dictionary node_properties
# node_label should be a string (with no spaces in between), node_properties should be a dictionary
def get_nodes(node_label, node_properties):
    i = 0
    result = []
    query_string = 'MATCH(label:' + node_label + '{'
    for node_property in node_properties:
        if i == 0:
            query_string += node_property + ': "' + node_properties[node_property] + '"'
        else:
            query_string += ', ' + node_property + ': "' + node_properties[node_property] + '"'
        i += 1
    query_string += '}) RETURN label'
    db = Database(db_url, db_name, db_password)
    for res in db.query(query_string):
        result.append(res['label'])
    return result


# returns a list of nodes properties
# node_label should be a string representing the "type" of the node
# e.g. MATCH(a:IP) RETURN keys(a)
def get_properties_labels(node_label):
    i = 0
    query_string = 'MATCH(a:' + node_label + ') RETURN keys(a)'

    db = Database(db_url, db_name, db_password)
    result = db.query(query_string)
    return result


# metoda vraća sve requestove koje je poslala ip adresa
def get_requests_for_ip(ip_address):
    query_string = 'MATCH(a:IP {ip_address: "' + ip_address + '"})-[:HAS_SENT]->(b:Log_line) RETURN b'
    db = Database(db_url, db_name, db_password)
    return db.query(query_string)

# metoda vraća sve jedinstvene ip adrese koje postoje u bazi
def get_count_of_ip():
    query_string = 'MATCH (p:IP) WITH DISTINCT p.ip_address as p RETURN count(p) as count'
    db = Database(db_url, db_name, db_password)
    ip_count = db.query(query_string)[0]['count']
    return ip_count

#metoda koja vraća listu 10 mapa ključ-country, vrijednost- broj sa najvećim brojem ip adresa
def get_Top_countries_by_ip():
    countries_dict = {}
    query_string = 'MATCH (n:IP) return DISTINCT n'
    db = Database(db_url, db_name, db_password)
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
    db = Database(db_url, db_name, db_password)
    response = db.query(query_string)
    response_list = []
    for i in response:
        response_list.append(i['n'])
    return response_list

#metoda za search po country code
def get_by_country_code(countryCode):
    query_string = 'MATCH (n) WHERE n.country="' + countryCode + '" RETURN n '
    db = Database(db_url, db_name, db_password)
    response = db.query(query_string)
    response_list = []
    for i in response:
        response_list.append(i['n'])
    return response_list

#metoda za search po country name - toga više nema!!
# def get_by_country_name(countryName):
#     query_string = 'MATCH (n) WHERE n.countryname="' + countryName + '" RETURN n '
#     db = Database(db_url, db_name, db_password)
#     response = db.query(query_string)
#     response_list = []
#     for i in response:
#         response_list.append(i['n'])
#     return response_list   

#metoda za search po city
def get_by_city(city):
    query_string = 'MATCH (n) WHERE n.city="' + city + '" RETURN n '
    db = Database(db_url, db_name, db_password)
    response = db.query(query_string)
    response_list = []
    for i in response:
        response_list.append(i['n'])
    return response_list   

#metoda za search po region
def get_by_region(region):
    query_string = 'MATCH (n) WHERE n.region="' + region + '" RETURN n '
    db = Database(db_url, db_name, db_password)
    response = db.query(query_string)
    response_list = []
    for i in response:
        response_list.append(i['n'])
    return response_list  

#metoda za search po org
def get_by_org(org):
    query_string = 'MATCH (n) WHERE n.org="' + org + '" RETURN n '
    db = Database(db_url, db_name, db_password)
    response = db.query(query_string)
    response_list = []
    for i in response:
        response_list.append(i['n'])
    return response_list  

#metoda za search po postal
def get_by_postal(postal):
    query_string = 'MATCH (n) WHERE n.postal="' + str(postal) + '" RETURN n '
    db = Database(db_url, db_name, db_password)
    response = db.query(query_string)
    response_list = []
    for i in response:
        response_list.append(i['n'])
    return response_list  

#metoda za search po timezone
def get_by_timezone(timezone):
    query_string = 'MATCH (n) WHERE n.timezone="' + timezone + '" RETURN n '
    db = Database(db_url, db_name, db_password)
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
    db = Database(db_url, db_name, db_password)
    return db.query(query_string)


# returns a list of all IP addresses and their properties
def get_all_ips():
    result_array = []
    query_string = 'MATCH(a:IP) RETURN a'
    db = Database(db_url, db_name, db_password)
    for res in db.query(query_string):
        result_array.append(res['a'])
    return result_array


# returns a list of all Servers and their properties
def get_all_servers():
    result_array = []
    query_string = 'MATCH(a:Server) RETURN a'
    db = Database(db_url, db_name, db_password)
    for res in db.query(query_string):
        result_array.append(res['a'])
    return result_array


# returns a list of all Log_lines and their properties
def get_all_log_lines():
    result_array = []
    query_string = 'MATCH(a:Log_line) RETURN a'
    db = Database(db_url, db_name, db_password)
    for res in db.query(query_string):
        result_array.append(res['a'])
    return result_array


# returns all data
def get_all():
    result_array = []
    query_string = 'MATCH(a) RETURN a'
    db = Database(db_url, db_name, db_password)
    for res in db.query(query_string):
        result_array.append(res['a'])
    return result_array





# returns a list of all relationships between ip adresses and log lines
def get_all_log_ip_relations(server_names, ips):
    result_array = []
    query_string = 'MATCH(a:IP)-[r]-(b:Log_line)-[]->(c:Server) '
    if server_names[0] == '' or ips[0] == '':
        query_string += " WHERE ("
    if server_names[0] != '':
        for i in range(len(server_names)):
            if i > 0:
                query_string += ' OR c.server_name = "' + server_names[i] + '" '
            else:
                query_string += ' c.server_name = "' + server_names[i] + '" '
    if server_names[0] == '' and ips[0] == '':
        query_string += ") AND ("
    if ips[0] != '':
        for i in range(len(ips)):
            if i > 0:
                query_string += ' OR a.ip_address = "' + ips[i] + '" '
            else:
                query_string += ' a.ip_address = "' + ips[i] + '" '
    query_string += ') RETURN a, r, b'
    db = Database(db_url, db_name, db_password)
    for res in db.query(query_string):
        result_array.append(res['r'])
    return result_array


# returns a list of all relationships between servers and log lines
def get_all_log_server_relations(server_names, ips):
    result_array = []
    query_string = 'MATCH(a:Server)-[r]-(b:Log_line)-[]->(c:Server) '
    if server_names[0] == '' or ips[0] == '':
        query_string += " WHERE ("
    if server_names[0] != '':
        for i in range(len(server_names)):
            if i > 0:
                query_string += ' OR c.server_name = "' + server_names[i] + '" '
            else:
                query_string += ' c.server_name = "' + server_names[i] + '" '
    if server_names[0] == '' and ips[0] == '':
        query_string += ") AND ("
    if ips[0] != '':
        for i in range(len(ips)):
            if i > 0:
                query_string += ' OR a.ip_address = "' + ips[i] + '" '
            else:
                query_string += ' a.ip_address = "' + ips[i] + '" '
    query_string += ') RETURN a, r, b'
    db = Database(db_url, db_name, db_password)
    for res in db.query(query_string):
        result_array.append(res['r'])
    return result_array


# creates a list of nodes for D3.js
def create_d3_nodes(server_names, ips):
    ip_nodes = get_d3_ips(server_names, ips)
    for ip in ip_nodes:
        ip['group'] = 0
        ip['name'] = ip['ip_address']

    all_nodes = ip_nodes.copy()
    logline_nodes = get_d3_loglines(server_names, ips)
    for line in logline_nodes:
        line['group'] = 1
        line['name'] = line['path']
        all_nodes.append(line)

    return all_nodes


# gets all ip nodes connected to the given server
def get_d3_ips(server_names, ips):
    # match(a:IP)-[]->(b:Log_line)-[]->(c:Server {server_name: "jackie"}) return a,b
    result_array = []
    query_string = 'MATCH(a:IP)-[]->(b:Log_line)-[]->(c:Server) '
    if server_names[0] == '' or ips[0] == '':
        query_string += " WHERE ("
    if server_names[0] != '':
        for i in range(len(server_names)):
            if i > 0:
                query_string += ' OR c.server_name = "' + server_names[i] + '" '
            else:
                query_string += ' c.server_name = "' + server_names[i] + '" '
    if server_names[0] == '' and ips[0] == '':
        query_string += ") AND ("
    if ips[0] != '':
        for i in range(len(ips)):
            if i > 0:
                query_string += ' OR a.ip_address = "' + ips[i] + '" '
            else:
                query_string += ' a.ip_address = "' + ips[i] + '" '
    query_string += ') return a'
    db = Database(db_url, db_name, db_password).query(query_string)
    if db:
        for res in db:
            result_array.append(res['a'])
    return result_array

def get_d3_loglines(server_names, ips):
    # match(a:IP)-[]->(b:Log_line)-[]->(c:Server {server_name: "jackie"}) return a,b
    result_array = []
    query_string = 'MATCH(a:IP)-[]->(b:Log_line)-[]->(c:Server) '
    if server_names[0] == '' or ips[0] == '':
        query_string += " WHERE ("
    if server_names[0] != '':
        for i in range(len(server_names)):
            if i > 0:
                query_string += ' OR c.server_name = "' + server_names[i] + '" '
            else:
                query_string += ' c.server_name = "' + server_names[i] + '" '
    if server_names[0] == '' and ips[0] == '':
        query_string += ") AND ("
    if ips[0] != '':
        for i in range(len(ips)):
            if i > 0:
                query_string += ' OR a.ip_address = "' + ips[i] + '" '
            else:
                query_string += ' a.ip_address = "' + ips[i] + '" '
    query_string += ') return b'
    db = Database(db_url, db_name, db_password).query(query_string)
    if db:
        for res in db:
            result_array.append(res['b'])
    return result_array


# creates a list of links for D3.js
def create_d3_links(server_names, ips):
    r1 = get_all_log_ip_relations(server_names, ips)
    res = []
    for relationship in r1:
        temp = []
        temp.append(relationship[0])
        temp.append(relationship[1])
        temp.append(relationship[2])
        res.append(temp)

    r2 = get_all_log_server_relations(server_names, ips)
    for relationship in r2:
        temp = []
        temp.append(relationship[0])
        temp.append(relationship[1])
        temp.append(relationship[2])
        res.append(temp)

    return res

def get_all_server_names():
    # match(a:Server) return a.server_name
    result_array = []
    query_string = 'MATCH(a:Server) RETURN a.server_name'
    db = Database(db_url, db_name, db_password)
    for res in db.query(query_string):
        result_array.append(res['a.server_name'])
    return result_array

# gets all ip nodes connected to the given server
def get_ips_by_server_name(server_names):
    # match(a:IP)-[]->(b:Log_line)-[]->(c:Server {server_name: "jackie"}) return a,b
    result_array = []
    query_string = 'MATCH(a:IP)-[]->(b:Log_line)-[]->(c:Server) '
    for i in range(len(server_names)):
        if i > 0:
            query_string += ' OR c.server_name = "' + server_names[i] + '" '
        else:
            query_string += ' WHERE c.server_name = "' + server_names[i] + '" '
    query_string += ' return a'
    db = Database(db_url, db_name, db_password).query(query_string)
    if db:
        for res in db:
            result_array.append(res['a'])
    return result_array
