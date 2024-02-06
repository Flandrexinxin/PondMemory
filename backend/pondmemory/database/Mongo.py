import pymongo
import config
from pondmemory.utils.Logger import logger

MONGO_HOST = config.MONGO_HOST
MONGO_PORT = config.MONGO_PORT
MONGO_DB = config.MONGO_DB


class Mongo:
    def __init__(self, 
                 host=MONGO_HOST, 
                 port=MONGO_PORT, 
                 database=MONGO_DB
                 ):
        self.host = host
        self.port = port 
        self.database = database
        self.client = None
    
    def get_client(self) -> pymongo.MongoClient:
        try:
            if self.client is None:
                self.client = pymongo.MongoClient(f'mongodb://{self.host}:{self.port}/')
                logger.logger.info(f"与MongoDB {self.host}:{self.port} 建立连接")
        except Exception as e:
            logger.logger.error(f"与MongoDB {self.host}:{self.port} 建立连接失败")
            logger.logger.error(e)
        return self.client

    def get_db(self):
        return self.get_client().get_database(self.database)

    def get_collection(self, collection: str):
        return self.get_db().get_collection(collection)

    def insert_one(self, collection: str, document: dict):
        collection = self.get_collection(collection)
        return collection.insert_one(document)

    def insert_many(self, collection: str, document: list):
        collection = self.get_collection(collection)
        return collection.insert_many(document)

    def find_one(self, collection: str, query: dict, ignore_id=True):
        collection = self.get_collection(collection)
        args = {}
        if ignore_id:
            args['_id'] = 0
        return collection.find_one(query, args)

    def find(self, collection: str, query: dict, ignore_id=True):
        collection = self.get_collection(collection)
        args = {}
        if ignore_id:
            args['_id'] = 0
        return collection.find(query, args)

    def update_one(self, collection: str, query: dict, value: dict):
        collection = self.get_collection(collection)
        return collection.update(query, value)

    def delete_one(self, collection: str, query: dict):
        collection = self.get_collection(collection)
        return collection.delete_one(query)

    def delete_many(self, collection: str, query: dict):
        collection = self.get_collection(collection)
        return collection.delete_many(query)







        



