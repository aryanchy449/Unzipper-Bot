# Copyright (c) 2022 Itz-fork

import os

class Config(object):
    # Mandotory
    APP_ID = int(os.environ.get("API_ID","23080322"))
    API_HASH = os.environ.get("API_HASH","b3611c291bf82d917637d61e4a136535")
    BOT_TOKEN = os.environ.get("BOT_TOKEN","6931048916:AAEiwn5cej-PVBw95cqsGskW-BEGx95o4jY")
    LOGS_CHANNEL = int(os.environ.get("LOGS_CHANNEL","-1002072662567"))
    BOT_OWNER = int(os.environ.get("BOT_OWNER","6214889840"))
    MONGODB_URL = os.environ.get("MONGODB_URL","mongodb+srv://hello:hello@cluster0.s7lxbia.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    GOFILE_TOKEN = os.environ.get("GOFILE_TOKEN","ETgJJ7ITuYFdVBSoamumKXuzKtWuKWYb")
    # Optional
    MAX_DOWNLOAD_SIZE = int(os.environ.get("1024*1024*6")) if os.environ.get("MAX_DOWNLOAD_SIZE") else 10737418240
    # Constents
    DOWNLOAD_LOCATION = f"{os.path.dirname(__file__)}/NexaBots"
    TG_MAX_SIZE = 2040108421
    CHUNK_SIZE = 1024 * 6
