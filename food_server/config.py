import os

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

TG_BOT_TOKEN = os.getenv('TG_BOT_TOKEN')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
