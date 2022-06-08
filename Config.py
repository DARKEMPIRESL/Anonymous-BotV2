from dotenv import load_dotenv
from os import path, getenv, mkdir
import os

ENVIRONMENT = bool(os.environ.get('ENVIRONMENT', False))

if path.exists("local.env"):
    load_dotenv("local.env")
else:
    load_dotenv()

if not path.exists("search"):
    mkdir("search")


class Configs:
    API_ID = int(getenv("API_ID", "0"))
    API_HASH = getenv("API_HASH", "abc123")
    BOT_TOKEN = getenv("BOT_TOKEN", "123:abc")
    OWNER_ID = int(getenv("OWNER_ID", "0123"))


config = Configs()
