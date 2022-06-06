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
	'CreoEngineEN', 'FTX_Official', 'stormwarfareHQ', 'seedifyfundofficial',
	'bycoinhunterduyuru', 'seedifyfund', 'sfundturkey', 'SpintopNetwork',
	'SpintopNetworkAnnouncements', 'pethereumchat', 'avalancheavax', 'avalaunch_app',
	'Avalaunch_Tr', 'STEPNofficial', 'movez_app', 'bfxtelegram', 'cryptonear',
	'pangolindexV2', 'talecraft', 'islanderofficial', 'HeroesChainedOfficial',
	'ImperiumEmpiresOfficial', 'COLONY_Announcement', 'maxi_xyz', 'GemGuardianOfficialChat',
	'cryowar', 'AstroSwapOfficial', 'unusdao', 'ProjectDegis', 'OneInchNetwork',
	'bountiehunterofficial', 'Airdrop', 'AirdropStar', 'OFFICIALairdropalert',
	'AirdropBSC_Com', 'Airdrop365Official', 'AirdropComet', 'VerifiedsAirdropOfficial',
	'Airdrops_Projects', 'AirdropS6', 'AirdropSupreme', 'AirdropStarship'
]

#############################
# Main Code                 #
#############################

if __name__ == "__main__":
	# Telegram instance
	tg = TelethonHelper(table='crypto', source_channels=source_channels)

	# Asenkron running
	asyncio.run(tg.get_participants())