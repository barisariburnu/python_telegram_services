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
	'ucretsiz_udemy_kurslariii', 'udemy', 'lorebeam', 'udemycoursesfree',
	'tutorialbar_udemy_coupons', 'ucretsiz_udemy_kurslari', 'UdemyFree4You',
	'udemyking1', 'Coursevania', 'Coursat2020', 'dwmfreecourses'
]

#############################
# Main Code                 #
#############################

if __name__ == "__main__":
	# Telegram instance
	tg = TelethonHelper(table='udemy', source_channels=source_channels)

	# Asenkron running
	asyncio.run(
		tg.get_participants()
	)