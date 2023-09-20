import numpy as np
import discord
from discord.ext import commands


col = discord.Color.blue()

class Maths(commands.Cog):

    @commands.group ()                                       # Making a group for other commands
    async def math(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send(f"```{ctx.subcommand_passed} doesn't belong to math\n\nFor more info on a specific command, use {'*help*'} command```")

    # * -------------------------------------------------------------------   

    @math.command ()
    async def add(self, ctx, *num : int):
        embed = discord.Embed(
            colour=col,
            title=f"Here's the sum: ```{sum(num)}```"
        )
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
        await ctx.send(embed = embed)        

    # * -------------------------------------------------------------------   

    @math.command ()
    async def subtract(self, ctx, *num : int):
        embed = discord.Embed(
            colour=col,
            title=f"Here's the difference: ```{num[0] - sum(num[1:])}```"
        )
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
        await ctx.send(embed = embed)        

    # * -------------------------------------------------------------------   
        
    @math.command ()
    async def multiply(self, ctx, *num : int):
        embed = discord.Embed(
            colour=col,
            title=f"Here's the output after multiplication: ```{np.prod(num)}```"
        )
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
        await ctx.send(embed = embed)     

    # * -------------------------------------------------------------------   

    @math.command ()
    async def divide(self, ctx, *num : int):
        if 0 in num[1:]:
            embed = discord.Embed(
                colour=col,
                title=f"Division by 0 is not allowed"
            )
            
        else:
            result = num[0]
            for n in num[1:]:
                result/=n        
            embed = discord.Embed(
                colour=col,
                title=f"Here's the output after division: ```{result}```"
            )
            
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
        await ctx.send(embed = embed)   
        
    # * -------------------------------------------------------------------   
            
    @math.command ()
    async def exponent(self, ctx, num1 : int, num2 : int):        
        embed = discord.Embed(
            colour=col,
            title=f"Here's the output after exponentiation: ```{pow(num1, num2)}```"
        )
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
        await ctx.send(embed = embed)        

    # * -------------------------------------------------------------------   

async def setup(bot):                           # Automatically called when we load an extension
    await bot.add_cog(Maths(bot))
