import os

ENVIRONMENT = os.environ.get('ENVIRONMENT', False)

class Config(object):

    API_ID = int(os.environ.get('API_ID', 0))
    API_HASH = os.environ.get('API_HASH', None)
    BOT_TOKEN = os.environ.get('BOT_TOKEN', None)
    OWNER_ID = os.environ.get('OWNER_ID', None)
    DATABASE_URL = os.environ.get("DATABASE_URL", None)





DEVS = [1120271521]

