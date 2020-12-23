from neo4j import GraphDatabase

# source: https://towardsdatascience.com/neo4j-cypher-python-7a919a372be7
class Database:
    def __init__(self, uri, user, pwd):
        self.__uri = uri
        self.__user = user
        self.__pwd = pwd
        self.__driver = None
        try:
            self.__driver = GraphDatabase.driver(self.__uri, auth=(self.__user, self.__pwd))
        except Exception as e:
            print("Failed to create the driver:", e)

    def close(self):
        if self.__driver is not None:
            self.__driver.close()

    #returns a dictionary if recordds exist
    def query(self, query, db=None):
        assert self.__driver is not None, "Driver not initialized!"
        session = None
        response = None
        try:
            session = self.__driver.session(database=db) if db is not None else self.__driver.session()
            response = session.run(query).data()

        except Exception as e:
            print("Query failed:", e)
        finally:
            if session is not None:
                session.close()
        return response
