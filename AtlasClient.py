from pymongo import MongoClient

class AtlasClient ():

    def __init__(self, altas_uri, dbname):
        self.mongodb_client = MongoClient(altas_uri)
        self.database = self.mongodb_client[dbname]

    def close_connection(self):
        self.mongodb_client.close()