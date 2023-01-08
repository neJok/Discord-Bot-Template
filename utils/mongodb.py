from motor.motor_asyncio import AsyncIOMotorClient

from config import MONGO_TOKEN, DATABASE_NAME, COLLECTION_NAME

class MongoDB:
    def __init__(self):
        # Connect to the database
        self.client = AsyncIOMotorClient(MONGO_TOKEN)
        
        self.db = self.client[DATABASE_NAME]
        self.collection = self.db[COLLECTION_NAME]

        print("Connected to MongoDB")

    async def count_documents(self, query = None):
        """Find count documents thats matches the query"""
        if not query:
            query = dict()
        return await self.collection.count_documents(query)

    async def insert_one(self, document):
        """Insert a document into the collection"""
        await self.collection.insert_one(document)

    async def find_one(self, query):
        """Find a single document that matches the query"""
        return await self.collection.find_one(query)

    async def update_one(self, query, update):
        """Update a single document that matches the query"""
        await self.collection.update_one(query, update)

    async def delete_one(self, query):
        """Delete a single document that matches the query"""
        await self.collection.delete_one(query)

    def close(self):
        """Close the connection to the database"""
        self.client.close()
