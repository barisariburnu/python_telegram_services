#!/usr/bin/env python3

#############################
# Imports                   #
#############################

from enum import Enum

#############################
# Status Model              #
#############################

class Status(Enum):
    INVALID = 0
    ALREADY = 1
    SUCCESS = 2
    ERROR = 3