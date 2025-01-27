import os
import asyncio
import discord
import logging

from config import DISCORD_TOKEN, PREFIX, OWNER_ID
from discord.ext import commands

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bot = commands.Bot(command_prefix=PREFIX, intents=discord.Intents.all(), help_command=None)

@bot.command()
async def sync_tree(ctx: commands.Context) -> None:
    if ctx.author.id != OWNER_ID:
        await ctx.message.add_reaction("❌")
        return
    
    await bot.tree.sync()
    await ctx.message.add_reaction("✅")

@bot.command()
async def load(ctx: commands.Context, extension: str) -> None:
    if ctx.author.id != OWNER_ID:
        await ctx.message.add_reaction("❌")
        return

    await bot.load_extension(f"cogs.{extension}")
    await ctx.message.add_reaction("✅")


@bot.command()
async def unload(ctx: commands.Context, extension: str) -> None:
    if ctx.author.id != OWNER_ID:
        await ctx.message.add_reaction("❌")
        return

    await bot.unload_extension(f"cogs.{extension}")
    await ctx.message.add_reaction("✅")


@bot.command()
async def reload(ctx: commands.Context, extension: str) -> None:
    if ctx.author.id != OWNER_ID:
        await ctx.message.add_reaction("❌")
        return

    await bot.unload_extension(f"cogs.{extension}")
    await bot.load_extension(f"cogs.{extension}")
    await ctx.message.add_reaction("✅")

async def main() -> None:
    async with bot:
        await load_extensions()
        await bot.start(DISCORD_TOKEN)


async def load_extensions() -> None:
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            print(f'Loading: {filename[:-3]}')
            await bot.load_extension(f"cogs.{filename[:-3]}")

    print('All extensions loaded.')


asyncio.run(main())
