#!/usr/bin/env python3

#############################
# Imports                   #
#############################

import asyncio

from libs.telegram import Telegram

#############################
# Global Variables          #
#############################

# Source telegram channel
source_channels = [
	'amazon', 'hotdealsofficials', 'Deals_Point', 'freebiehunter', 'AliexpressHotdeals12',
	'uk_hot_deals', 'aliexpressbroficial', 'AliexpressEvaShop'
]

#############################
# Main Code                 #
#############################

if __name__ == "__main__":
	# Telegram instance
	tg = Telegram(table='udemy', source_channels=source_channels)

	# Asenkron running
	asyncio.run(tg.main())