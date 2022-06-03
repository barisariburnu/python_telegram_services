#!/usr/bin/env python3

#############################
# Imports                   #
#############################

import os
import asyncio
import logging

from telethon.sync import TelegramClient
from python_telegram_services.models.user import User
from python_telegram_services.models.status import Status
from python_telegram_services.libs.config import QUERIES, TELEGRAM_API_ID, TELEGRAM_API_HASH

#############################
# Global Variables          #
#############################

# Get logger
logger = logging.getLogger(__name__)

# Script name
filename = os.path.basename(__file__)
script_name = os.path.splitext(filename)[0]

# Source telegram channel
source_channels = [
    'ucretsiz_udemy_kurslariii', 'udemy', 'lorebeam', 'udemycoursesfree',
    'tutorialbar_udemy_coupons', 'ucretsiz_udemy_kurslari', 'UdemyFree4You',
    'udemyking1', 'Coursevania', 'Coursat2020', 'dwmfreecourses'
]

#############################
# Configuration             #
#############################

# Setup handler
logger.addHandler(logging.StreamHandler())

# Set logging level
logger.setLevel(logging.DEBUG)

# Telegram Configuration
client = TelegramClient(script_name, TELEGRAM_API_ID, TELEGRAM_API_HASH)

#############################
# Main Code                 #
#############################

async def main():
    async with client:
      for channel in source_channels:
        for key in QUERIES:
          try:
            async for user in client.iter_participants(channel, search=key):
                user = User(user, channel=channel)
                result = user.save(table='udemy')

                if result == Status.INVALID:
                    logger.debug(f"INVALID \t [Channel: {user.channel} > Key: {key} > User: {user.username}]")
                elif result == Status.ALREADY:
                    logger.debug(f"EXISTS \t [Channel: {user.channel} > Key: {key} > User: {user.username}]")
                elif result == Status.ERROR:
                    logger.debug(f"ERROR \t [Channel: {user.channel} > Key: {key} > User: {user.username}]")
                elif result == Status.SUCCESS:
                    logger.debug(f"SUCCESS \t [Channel: {user.channel} > Key: {key} > User: {user.username}]")

          except TypeError as e:
            logger.error(e)
            continue
          except Exception as e:
            logger.error(e)
            continue

if __name__ == "__main__":
    asyncio.run(main())