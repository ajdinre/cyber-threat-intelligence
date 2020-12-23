from .neo4j_db import Database

#metoda stvara novi cvor u bazi tipa class_name
# koji ima sve atribute zadane dictionaryjem attributes
#stvara cvor 'class_name' sa atributima 'attributes'
#class_name je string, a attributes je dictionary
def create_node(class_name, attributes):
    i = 0
    query_string = 'CREATE(label' + ':' + class_name + '{'
    for attribute in attributes:
        if i == 1:
            query_string += attribute + ': "' + attributes[attribute] + '"'
        elif i > 1:
            query_string += ', ' + attribute + ': "' + attributes[attribute] + '"'
        i += 1
    query_string += '}) RETURN label'

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
    return db.query(query_string)
#example
#mydict = {
#    "datetime": "30/Aug/2020:03:24:31",
#        "method": "GET"
#}
#print(test('Request', mydict))

# metoda vraća sve requestove koje je poslala ip adresa
def get_requests_for_ip(ip_address):
    query_string = 'MATCH(a:Ip {address: "' + ip_address + '"})-[:HAS_SENT]->(b:Request) RETURN b'
    db = Database("bolt://localhost:7687", "neo4j", "password")
    return db.query(query_string)