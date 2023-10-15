import discord 
import random
import peewee
from discord.ext import commands
from models.account import Account


col = discord.Color.purple()

class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# * -------------------------------------------------------------------   

    @commands.command()
    async def cflip(self, ctx, choice: str, amount: int):
        try:
            account = Account.get(Account.user_id == ctx.message.author.id, Account.guild_id == ctx.message.guild.id)
        except peewee.DoesNotExist:
            account = Account.create(user_id = ctx.message.author.id, guild_id = ctx.message.guild.id, amount  = 100)
        
        if amount > account.amount:
             embed = discord.Embed(
                description=f"You do not have enough credits!",
                color=col
            )
        
        heads = random.randint(0,1)            # 0 means tails and 1 means heads
        won = False
        if heads and choice.lower().startswith("h"):
            won = True
            account.amount += amount
        elif not heads and choice.lower().startswith("t"):
            won = True
            account.amount += amount
        else:
            account.amount -= amount
        
        account.save()
        if won:
            embed = discord.Embed(
                title=f"**{ctx.author.display_name}** has won the coin flip ^o^!",
                description=f"Your current balance: {account.amount}",
                color=col
            )
            embed.set_author(name='Coin Flip')
            embed.set_footer(text = "This command doesn't have any cooldown")
        
        if not won:
            embed = discord.Embed(
                title=f"**{ctx.author.display_name}** just lost the coin flip... :c!",
                description=f"Your current balance: {account.amount}",
                color=col
            )
            embed.set_author(name='Coin Flip')
            embed.set_footer(text = "This command doesn't have any cooldown")
        
        await ctx.send(embed = embed)

# * -------------------------------------------------------------------   

    @commands.command()
    async def balance(self, ctx):
        account = Account.fetch(ctx.message)
        embed = discord.Embed(
            title=f"{ctx.author.display_name}'s Current Balance",
            description=f"The current balance of this user.",
            color=col
        )
        embed.add_field(name="Current Balance:", value=f"**{account.amount}**")
        embed.set_footer(text="Want to increase balance? Try running some economy based commands")
        embed.set_thumbnail(url = ctx.author.display_avatar.url)

        await ctx.send(embed = embed)
        
# * -------------------------------------------------------------------   

    @commands.cooldown(1, per = 600)
    @commands.command()
    async def beg(self, ctx):
        account = Account.fetch(ctx.message)
        
        change_val = random.randint(-50, 100)
        prev = account.amount
        account.amount += change_val
        
        account.save()
        
        if account.amount < prev:
            embed = discord.Embed(
                title=f"Oh No! - You have been robbed!",
                description=f"A group of robbers saw oppertunity in taking advantage of you.",
                color=discord.Color.red()
            )
            embed.add_field(name="Amount robbed:", value=f"**{abs(change_val)}**", inline = False)
            embed.add_field(name="New Balance:", value=f"**{account.amount}**", inline = False)
            embed.set_footer(text="Should probably beg in a nicer part of town...")
            embed.set_thumbnail(url = ctx.author.display_avatar.url)
            await ctx.send(embed = embed)
            
        elif account.amount > prev:
            embed = discord.Embed(
            title=f"Oh Sweet Green!",
                description=f"Some kind souls have given you what they could.",
                color=discord.Color.green()
            )
            embed.add_field(name="Amount gained:", value=f"**{change_val}**", inline = False)
            embed.add_field(name="New Balance:", value=f"**{account.amount}**", inline = False)
            embed.set_footer(text="Want more? Wait 10 minutes to run this command again, or try some other commands!")
            embed.set_thumbnail(url = ctx.author.display_avatar.url)
            await ctx.send(embed = embed)
            
        elif account.amount == prev:
            embed = discord.Embed(
            title=f"Awh That Sucks!",
                description=f"Looks like begging didn't get you anywhere today",
                color=discord.Color.green()
            )
            embed.add_field(name="Amount gained:", value=f"**{change_val}**", inline = False)
            embed.add_field(name="New Balance:", value=f"**{account.amount}**", inline = False)
            embed.set_footer(text="Want more? Wait 10 minutes to run this command again, or try some other commands!")
            embed.set_thumbnail(url = ctx.author.display_avatar.url)
            await ctx.send(embed = embed)

# * -------------------------------------------------------------------   

    @commands.cooldown(1, per = 3600)
    @commands.command()
    async def work(self, ctx):
        account = Account.fetch(ctx.message)
        paid = random.randint(200, 500)
        account.amount += paid
        account.save()
        
        embed = discord.Embed(
            title="Phew!",
            description="After a tiring shift, here's your earning!",
            color=discord.Color.green()
        )
        embed.add_field(name="Earnings:", value=f"**{paid}**", inline=False)
        embed.add_field(name="New Balance:", value=f"**{account.amount}**")
        embed.set_footer(text="Want more? Wait 1 hour to run this command again, or try some other commands!")
        embed.set_thumbnail(url = ctx.author.display_avatar.url)
        await ctx.send(embed = embed)
        
# * -------------------------------------------------------------------   
        
        
async def setup(bot):
    await bot.add_cog(Economy(bot))
    