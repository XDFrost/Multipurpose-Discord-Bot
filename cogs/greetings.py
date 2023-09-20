import discord
from discord.ext import commands

col = discord.Color.blue()

class Greetings(commands.Cog):
    
    # self is used to change the instance of a object

    @commands.command()
    async def hello(self, ctx, *, member: discord.Member):
        embed = discord.Embed(
            color=col,
            title=f"Hello {member.display_name}"
        )
        
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
        await ctx.send(embed = embed)


async def setup(bot):
    await bot.add_cog(Greetings(bot))
    