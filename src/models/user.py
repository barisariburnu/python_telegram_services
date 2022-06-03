#!/usr/bin/env python3

#############################
# Imports                   #
#############################

from pymongo import MongoClient
from libs.config import MONGO_USERNAME, MONGO_PASSWORD
from models.status import Status

#############################
# Configuration             #
#############################

# Mongo DB Configuration
client = MongoClient(f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@ireland-shard-00-00.xjelg.mongodb.net:27017,ireland-shard-00-01.xjelg.mongodb.net:27017,ireland-shard-00-02.xjelg.mongodb.net:27017/?ssl=true&replicaSet=atlas-nrk72v-shard-0&authSource=admin&retryWrites=true&w=majority")

# Get database
db = client.telegram

#############################
# User Model                #
#############################

class User:
    def __init__(self, data, channel=None) -> None:
        self._id = data.id
        self.channel = channel
        self.username = data.username
        self.first_name = data.first_name
        self.last_name = data.last_name

    def save(self, table) -> Status:
        if not self.username:
            return Status.INVALID

        if db[table].find_one({"$and": [{"_id": self._id}, {"channel": self.channel}]}):
            return Status.ALREADY

        if str(db[table].insert_one(self.__dict__)):
            return Status.SUCCESS
        else:
            return Status.ERROR