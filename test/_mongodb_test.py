import pymongo
from luigi.mongo import MongoTarget
import datetime
import unittest

host = 'localhost'
port = 27017
database = 'testdatabase'
collection = 'testcollection'

def _insert_to_test_collection():
    client = MongoClient(host, port)
    collection = client[database][collection]
    collection.insert({"timestamp": datetime.datetime.now()})
