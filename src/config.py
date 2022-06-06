#!/usr/bin/env python3

import os

MONGO_USERNAME = os.environ['MONGO_USERNAME']
MONGO_PASSWORD = os.environ['MONGO_PASSWORD']

TELEGRAM_API_ID = os.environ['TELEGRAM_API_ID']
TELEGRAM_API_HASH = os.environ['TELEGRAM_API_HASH']
TELEGRAM_BOT_TOKEN = os.environ['TELEGRAM_BOT_TOKEN']

QUERIES = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','0','1',
    '2','3','4','5','6','7','8','9',' ','','~', ':', "'", '+', '[', '\\', 
    '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', 
    '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/'
]