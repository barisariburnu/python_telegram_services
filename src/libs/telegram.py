#!/usr/bin/env python3

#############################
# Imports                   #
#############################

import logging

from telethon.sync import TelegramClient
from models.user import User
from models.status import Status
from libs.config import QUERIES, TELEGRAM_API_ID, TELEGRAM_API_HASH

#############################
# Global Variables          #
#############################

# Get logger
logger = logging.getLogger(__name__)

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

async def main(table, source_channels):
	async with client:
		for channel in source_channels:
			for key in QUERIES:
				try:
					async for user in client.iter_participants(channel, search=key):
						user = User(user, channel=channel)
						result = user.save(table=table)
						
						if result == Status.INVALID:
							logger.debug(f"INVALID \t [Channel: {user.channel} > Key: {key} > User: {user.username}]")
						elif result == Status.ALREADY:
							logger.debug(f"EXISTS \t [Channel: {user.channel} > Key: {key} > User: {user.username}]")
						elif result == Status.ERROR:
							logger.debug(f"ERROR \t [Channel: {user.channel} > Key: {key} > User: {user.username}]")
						elif result == Status.SUCCESS:
							logger.debug(f"SUCCESS \t [Channel: {user.channel} > Key: {key} > User: {user.username}]")

		  		except ChatAdminRequiredError as e:
			  		logger.error(e)
			  		continue
		  		except TypeError as e:
					logger.error(e)
					continue
		  		except Exception as e:
					logger.error(e)
					continue