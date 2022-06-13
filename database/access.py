from config import Config
from database.database import Database

dark = Database(Config.DATABASE_URL, Config.SESSION_NAME)
