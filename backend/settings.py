import os
from dotenv import load_dotenv

load_dotenv()

# Flask app variables

DB_NAME = os.getenv("DB_NAME")
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DEBUG = True
TESTING = True

DBTEST_NAME = os.getenv("DBTEST_NAME")
DBTEST_USER = os.getenv("DBTEST_USER")
DBTEST_PASSWORD = os.getenv("DBTEST_PASSWORD")

# API Client variables
RAWG_API_KEY = os.getenv("RA_APIKEY")
IGDB_CLIENT_ID = os.getenv("IG_CID")
IGDB_CLIENT_SECRET = os.getenv("IG_CSECRET")
TS_TOKEN = os.getenv("TS_TOKEN")
