import os

from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")

OWNER_ID = int(os.getenv("OWNER_ID"))
PREFIX = os.getenv("BOT_PREFIX")

print(DATABASE_NAME)
cluster = AsyncIOMotorClient(MONGO_URI)
db = cluster[DATABASE_NAME]
