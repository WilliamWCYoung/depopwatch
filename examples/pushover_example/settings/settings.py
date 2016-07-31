# settings.py
from os.path import join, dirname
from os import environ
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

PUSHOVER_API_TOKEN = environ.get("PUSHOVER_API_TOKEN")
PUSHOVER_CLIENT_KEY = environ.get("PUSHOVER_CLIENT_KEY")
