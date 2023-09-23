import discord
from discord.ext import commands
from datetime import datetime


col = discord.Color.blue()

async def is_owner(ctx):
    return ctx.author.id == ctx.guild.owner.id

class Miscellaneous(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        
    @commands.command ()
    async def invite(self, ctx, who : discord.Member):
        joined_at = who.joined_at.strftime("%Y-%m-%d at %H:%M")
        embed = discord.Embed(
            colour=col,
            title=f"{who.display_name} joined at {joined_at}"                        # display_name displays the server name of the author not their tag name   
        )
        
        embed.set_author(name = ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
        
        await ctx.send(embed = embed)                  
          
# * -------------------------------------------------------------------   
        
    @commands.command ()
    async def joined(self, ctx, who : discord.Member):
        joined_at = who.joined_at.strftime("%Y-%m-%d at %H:%M")
        embed = discord.Embed(
            colour=col,
            title=f"{who.display_name} joined at {joined_at}"                        # display_name displays the server name of the author not their tag name   
        )
        
        embed.set_author(name = ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
        
        await ctx.send(embed = embed)                  
          
# * -------------------------------------------------------------------   
    
    @commands.command()
    @commands.check(is_owner)
    async def load(self, ctx, cog: str):
        try: 
            self.bot.load_extension(f"cogs.{cog.lower()}")
            await ctx.send(f"```Loaded cog: {cog}```")
        except commands.ExtensionNotFound:
            await ctx.send(f"```Cog not found: {cog}```")
        except commands.ExtensionAlreadyLoaded:
            await ctx.send(f"```Cog already loaded: {cog}```")
    
# * -------------------------------------------------------------------   
       
    @commands.command()
    @commands.check(is_owner)
    async def unload(self, ctx, cog: str):
        try:
            await self.bot.unload_extension(f"cogs.{cog.lower()}")
            await ctx.send(f"```Unloaded cog: {cog}```")
        except commands.ExtensionNotLoaded:
            await ctx.send(f"```Cog not loaded: {cog}```")

# * -------------------------------------------------------------------   

    # Error handling for load and unload
    @load.error
    @unload.error
    async def say_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("```Permission Denied!```")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("```Missing required argument.```")
        else:
            await ctx.send(f"```An error occurred: {error}```")
        raise error
            
# * -------------------------------------------------------------------   
    

async def setup(bot):
    await bot.add_cog(Miscellaneous(bot))
    