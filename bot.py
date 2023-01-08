import discord
from discord.ext import commands

import os
import asyncio

# These are constants that are used throughout the code
# DISCORD_TOKEN is the API token for the Discord bot
# PREFIX is the command prefix that the bot uses
# APPLICATION_ID is the application ID for the Discord bot
# OWNER_ID is the Discord user ID for the owner of the bot
from config import DISCORD_TOKEN, PREFIX, APPLICATION_ID, OWNER_ID

# Create a new Discord bot with the specified command prefix and intents
bot = commands.Bot(command_prefix=PREFIX, intents=discord.Intents.all(), 
                   help_command=None, application_id=APPLICATION_ID)

# This is a command that loads a cog (a module containing commands)
@bot.command()
async def load(ctx, extension):
    # Check if the user who ran the command is the bot owner
    if ctx.author.id == OWNER_ID:
        # Load the cog
        await bot.load_extension(f"cogs.{extension}")
        await ctx.send("Load")

# This is a command that unloads a cog
@bot.command()
async def unload(ctx, extension):
    # Check if the user who ran the command is the bot owner
    if ctx.author.id == OWNER_ID:
        # Unload the cog
        await bot.unload_extension(f"cogs.{extension}")
        await ctx.send("Unload")

# This is a command that reloads a cog
@bot.command()
async def reload(ctx, extension):
    # Check if the user who ran the command is the bot owner
    if ctx.author.id == OWNER_ID:
        # Unload and then load the cog
        await bot.unload_extension(f"cogs.{extension}")
        await bot.load_extension(f"cogs.{extension}")
        await ctx.send("Reload")

# This is the main function that starts the bot
async def main():
    # Open a "context" for the bot
    async with bot:
        # Load all cogs
        await load_extensions()
        # Start the bot
        await bot.start(DISCORD_TOKEN)

# This function loads all cogs in the "cogs" directory
async def load_extensions():
    # Iterate through all filenames in the "cogs" directory
    for filename in os.listdir("./cogs"):
        # Check if the file is a Python file
        if filename.endswith(".py"):
            # Load the cog
            print(f'Load: {filename[:-3]}')
            await bot.load_extension(f"cogs.{filename[:-3]}")
    print('All cogs loaded.')

# Run the main function
asyncio.run(main())