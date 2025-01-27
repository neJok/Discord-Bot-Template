import discord

from discord import app_commands
from discord.ext import commands
from motor.motor_asyncio import AsyncIOMotorClient

from config import db


class SampleCog(commands.Cog):
    def __init__(self, bot: commands.Bot, db: AsyncIOMotorClient) -> None:
        self.bot = bot
        self.db = db

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        print(await self.db.your_database.count_documents({})) # Example of using database queries
        print(f"Bot {self.bot.user} ready in Discord.")
    
    @app_commands.guild_only()
    @app_commands.command(name="test_command", description="Test command description")
    async def inventory(self, intreaction: discord.Interaction) -> None:
        await intreaction.response.send_message("Test command work!")

async def setup(bot) -> None:
    await bot.add_cog(SampleCog(bot, db))
