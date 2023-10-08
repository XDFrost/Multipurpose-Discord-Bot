import discord
from discord.ext import commands, tasks
import json
import asyncio
import math


class LevelSystem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.save.start()
    
        with open("cogs/json/users.json", "r") as f:
            self.users = json.load(f)
 
    @tasks.loop(seconds=5)
    async def save(self):
        # await self.bot.wait_until_ready()
        # while not self.bot.is_closed():
        with open("cogs/json/users.json", "w") as f:
            json.dump(self.users, f, indent=4)
        
              
    def level_up(self, author_id):
        current_xp = self.users[author_id]["Experience"]
        current_level = self.users[author_id]["Level"]
        
        if current_xp >= math.ceil((10 * (current_level ** 4)) / 2):
            self.users[author_id]["Level"] += 1
            return True
        else:
            return False
        
# * -------------------------------------------------------------------   

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == self.bot.user.id:
            return
        
        author_id = str(message.author.id)
        
        if not author_id in self.users:
            self.users[author_id] = {}
            self.users[author_id]["Level"] = 0
            self.users[author_id]["Experience"] = 0
            
        xp = 5
        self.users[author_id]["Experience"] += xp
        
        if self.level_up(author_id):
            level_up_embed = discord.Embed( title = "Woohoo - Leveled Up!", color=discord.Color.blue())
            level_up_embed.set_author(name = message.author.display_name, icon_url=message.author.display_avatar.url)
            level_up_embed.add_field(name = "Congratulations", value=f"{message.author.mention} has leveled up to level `{self.users[author_id]['Level']}` !")
        
            sent = await message.channel.send(embed = level_up_embed)
            sent
            await asyncio.sleep(10)
            await sent.delete()

# * -------------------------------------------------------------------   

    @commands.command(aliases = ["rank", "lvl"])
    async def level(self, ctx, user: discord.User = None):
        if user is None:
            user = ctx.author
        elif user is not None:
            user = user
            
        level_card = discord.Embed(title=f"{user.name}'s Level and Experience", color = discord.Color.blue())
        level_card.add_field(name = "Level: ", value=self.users[str(user.id)]["Level"])
        level_card.add_field(name = "Experience: ", value=self.users[str(user.id)]["Experience"])
        level_card.set_footer(text=f"Requested by {ctx.author.name}")
        
        await ctx.send(embed = level_card)
        
# * -------------------------------------------------------------------   

async def setup(bot):
    await bot.add_cog(LevelSystem(bot))
