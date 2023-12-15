import discord
from discord.ext import commands
from models.player_stats import Stats



col = discord.Color.purple()

class RPG(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# * -------------------------------------------------------------------




# * -------------------------------------------------------------------

async def setup(bot):
    await bot.add_cog(RPG(bot))
    