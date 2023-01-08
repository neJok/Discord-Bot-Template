import os
from dotenv import load_dotenv

# Load from .env file
load_dotenv()

# Load Discord token from .env file
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Load application ID from .env file
APPLICATION_ID = int(os.getenv("APPLICATION_ID"))

# Set owner ID
OWNER_ID = 1

# Set command prefix
PREFIX = "!"

# Load MongoDB connection token from .env file
MONGO_TOKEN = os.getenv("MONGO_TOKEN")

# Set name of database to use
DATABASE_NAME = "mydatabase"

# Set name of collection to use
COLLECTION_NAME = "mycollection"