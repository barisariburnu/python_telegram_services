#!/usr/bin/env python3

#############################
# Imports                   #
#############################

import asyncio

from libs.telegram import main

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
    asyncio.run(
		main(table='amazon', source_channels=source_channels)
	)