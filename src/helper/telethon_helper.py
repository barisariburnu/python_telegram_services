#!/usr/bin/env python3

#############################
# Imports                   #
#############################

import os
import logging

from telethon.sync import TelegramClient
from telethon.errors import ChatAdminRequiredError
from models.user import User
from models.status import Status
from config import QUERIES, TELEGRAM_API_ID, TELEGRAM_API_HASH

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

#############################
# Main Code                 #
#############################

class TelethonHelper:
	def __init__(self, table, source_channels):
		self.table = table
		self.source_channels = source_channels
		self.client = TelegramClient(f"telethon_{self.table}", TELEGRAM_API_ID, TELEGRAM_API_HASH)

	async def main(self):
		async with self.client:
			for channel in self.source_channels:
				for key in QUERIES:
					try:
						async for user in self.client.iter_participants(channel, search=key):
							user = User(user, channel=channel)
							result = user.save(table=self.table)

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