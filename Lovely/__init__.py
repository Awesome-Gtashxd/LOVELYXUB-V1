import os
import time
import logging
import motor.motor_asyncio

from pyrogram import Client
from pymongo import MongoClient

FORMAT = "[Lovely]: %(message)s"

logging.basicConfig(level=logging.INFO, handlers=[logging.FileHandler('logs.txt'), logging.StreamHandler()], format=FORMAT)

StartTime = time.time()
MODULE = []

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time

# Setting logging
logger = logging.getLogger(__name__)

# Setting database connection
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://tiwarireeta004:peqxLEd36RAg7ors@cluster0.furypd3.mongodb.net/?retryWrites=true&w=majority")

# Settion bot configurations
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
STRING_SESSION = os.getenv("STRING_SESSION")
BOT_TOKEN = os.getenv("BOT_TOKEN")
DATABASE_NAME = os.getenv("DATABASE_NAME", "LovelyXUB")

cli = motor.motor_asyncio.AsyncIOMotorClient(DATABASE_URL)
db = cli[DATABASE_NAME]

DB = MongoClient(DATABASE_URL)
DATABASE = DB[DATABASE_NAME]

# Master Client Using Pyrogram
lovely = Client(name="Lovely", session_string=STRING_SESSION, api_id=API_ID, api_hash=API_HASH, plugins=dict(root="Lovely"))

# Bot Client Using Pyrogram
bot = Client(name="LovelyX", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH, plugins=dict(root="Lovely"))

class INFO:
   def lovely():
      info = lovely.get_me()
      return info   
     
   def bot():
      info = bot.get_me()
      return info
