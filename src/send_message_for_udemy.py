#!/usr/bin/env python3

#############################
# Imports                   #
#############################

import logging

from pyrogram import Client
from pymongo import MongoClient, ASCENDING, DESCENDING
from pyrogram import enums
from pyrogram.types import (InlineKeyboardMarkup, InlineKeyboardButton)
from pymongo import MongoClient
from config import MONGO_USERNAME, MONGO_PASSWORD
from models.status import Status
from models.course import Course
from config import TELEGRAM_API_HASH, TELEGRAM_API_ID, TELEGRAM_BOT_TOKEN

#############################
# Global Variables          #
#############################

# Get logger
logger = logging.getLogger(__name__)

TARGET_CHANNEL = 'freeudemydiscounts'

#############################
# Configuration             #
#############################

# Setup handler
logger.addHandler(logging.StreamHandler())

# Set logging level
logger.setLevel(logging.DEBUG)

# Mongo DB Configuration
client = MongoClient(f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@ac-dczxfng-shard-00-00.latzb7l.mongodb.net:27017,ac-dczxfng-shard-00-01.latzb7l.mongodb.net:27017,ac-dczxfng-shard-00-02.latzb7l.mongodb.net:27017/?ssl=true&replicaSet=atlas-bwqagz-shard-0&authSource=admin&retryWrites=true&w=majority")

app = Client(
  f"pyrogram_{TARGET_CHANNEL}",
  api_id=TELEGRAM_API_ID, 
  api_hash=TELEGRAM_API_HASH,
  bot_token=TELEGRAM_BOT_TOKEN
)

#############################
# Udemy Model               #
#############################

class Udemy:
    def __init__(self) -> None:
        self.cursor = client.udemy['course']
        self.target_channel = TARGET_CHANNEL

    def update(self, data) -> Status:
        try:
            if str(
                self.cursor.update_one(
                    {"_id": data.id}, 
                    {'$set': { 'shared': data.shared + 1 }},
                    upsert=False)
                ):
                return Status.SUCCESS
            else:
                return Status.ERROR
        except Exception as e:
            return Status.ERROR
    
    async def send_photo(self):
        async with app:
            try:
                result = self.cursor.find({}).sort([("shared", ASCENDING), ("created", DESCENDING)]).limit(1)[0]
                data = Course(result)
                
                response = await app.send_photo(
                    self.target_channel,
                    data.image_url,
                    caption=data.caption,
                    parse_mode=enums.ParseMode.MARKDOWN,
                    reply_markup=InlineKeyboardMarkup(
                        [[
                            InlineKeyboardButton("ENROLL NOW", url=data.shorten_url)
                        ]]
                    )
                )

                if hasattr(response, 'id'):
                    result = self.update(data)
                    if result:
                        logger.debug(f"SUCCESS \t [Course: {data.title}]")
                    else:
                        logger.debug(f"ERROR \t [Course: {data.title}]")
                else:
                    logger.debug(f"ERROR \t [Course: {data.title}]")
            except Exception as e:
                logger.debug(f"ERROR \t [{e}]")

if __name__ == "__main__":
	udemy = Udemy()
	app.run(udemy.send_photo())