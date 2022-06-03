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
    'ucretsiz_udemy_kurslariii', 'udemy', 'lorebeam', 'udemycoursesfree',
    'tutorialbar_udemy_coupons', 'ucretsiz_udemy_kurslari', 'UdemyFree4You',
    'udemyking1', 'Coursevania', 'Coursat2020', 'dwmfreecourses'
]

#############################
# Main Code                 #
#############################

if __name__ == "__main__":
    asyncio.run(
		main(table='udemy', source_channels=source_channels)
	)