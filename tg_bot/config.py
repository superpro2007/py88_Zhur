from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.

TG_BOT_TOKEN = os.getenv('TG_BOT_TOKEN')