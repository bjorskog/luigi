import pymongo
from luigi.mongo import MongoTarget
import datetime
import unittest

host = 'localhost'
port = 27017
database = 'testdatabase'
collection = 'testcollection'

class MongoTargetTest(unittest.TestCase):
    """ testing the mongo-target extension """
    def setUp(self):
        self.client = pymongo.MongoClient(host, port)
        self.collection = self.client[database][collection]
        self.target = MongoTarget(database, collection)

    def test_insert(self):
        collection = self.collection
        collection.insert({"timestamp": datetime.datetime.now()})
        
    def test_exists(self):
        self.target.exists()

    def test_not_exists(self):
        pass
    
