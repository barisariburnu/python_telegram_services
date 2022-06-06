#!/usr/bin/env python3

#############################
# Imports                   #
#############################

import asyncio

from helper.telethon_helper import TelethonHelper

#############################
# Global Variables          #
#############################

# Source telegram channel
source_channels = [
	'amazonnv', 'hotdealsofficials', 'Deals_Point', 'freebiehunter', 'AliexpressHotdeals12',
	'uk_hot_deals', 'aliexpressbroficial', 'AliexpressEvaShop', 'Amazon_Deals_Flipkart_Loots13',
	'Amazon_Movies_Videos_hd_Movies', 'Amazon_Movies_Videos_hd_prime'
]

#############################
# Main Code                 #
#############################

if __name__ == "__main__":
	# Telegram instance
	tg = TelethonHelper(table='amazon', source_channels=source_channels)

	# Asenkron running
	asyncio.run(tg.get_participants())