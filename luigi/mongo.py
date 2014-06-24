# Copyright (c) 2012 Spotify AB
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.

import pymongo

class MongoTarget(object):
    """ An extension of the Target class for writing to MongoDB. """

    def __init__(self, database, collection, host='localhost', port=27017):
        """ initialization """
        self.client = pymongo.MongoClient(host, port)
        self.database = self.client[database]
        self.collection = self.database[collection]

    def exists(self):
        """ checks if the document exists in the collection """
        return False

    def insert(self, doc):
        """ will insert a document to the collection """
        self.collection.insert(doc)
