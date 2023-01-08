from discord.ext import commands
from utils import mongodb

# This class is a Cog for the Discord bot, which contains various commands and listeners.
class SampleCog(commands.Cog):
	# The `__init__` function is run when the Cog is created.
	# It sets the bot and database instance variables.
	def __init__(self, bot):
		self.bot = bot
		self.db = mongodb.MongoDB()

	# This is an event listener that will be called when the Discord bot is ready.
	@commands.Cog.listener()
	async def on_ready(self):
		# Print a message indicating that the bot is ready.
		print(f"Bot {self.bot.user} ready in Discord.")
		# Print the number of documents in the database.
		print(await self.db.count_documents())

# This function adds the SampleCog to the bot.
async def setup(bot):
	await bot.add_cog(SampleCog(bot))