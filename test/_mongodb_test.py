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
        self.target = MongoTarget(database, collection)
        self.doc = { "timestamp":datetime.datetime.now() }
        
    def test_insert(self):
        self.target.insert(self.doc)
        
    def test_exists(self):
        self.target.exists()
