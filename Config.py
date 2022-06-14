import os

from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())


class Config(object):

    API_ID = int(os.environ.get('API_ID', 0))
    API_HASH = os.environ.get('API_HASH', None)
    BOT_TOKEN = os.environ.get('BOT_TOKEN', None)
    OWNER_ID = os.environ.get('OWNER_ID', None)
    REDIS_URI = os.getenv("REDIS_URI", None)
    REDIS_PASS = os.getenv("REDIS_PASS", None)





DEVS = [1120271521]

