import discord 
import asyncio
from discord.ext import commands
import json


timeout = 10

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
# * -------------------------------------------------------------------

    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def purge(self, ctx, count: int):
        await ctx.channel.purge(limit = count+1)
        embed = discord.Embed(title=f"{count} message(s) have been deleted", color=discord.Color.blue())
        embed.set_author(name = ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
        
        message = await ctx.send(embed = embed)
        message
        await asyncio.sleep(timeout)
        await message.delete()
    
# * -------------------------------------------------------------------

    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, member: discord.Member, *, modreason):
        await ctx.guild.kick(member)
        conf_embed = discord.Embed(
            title=f"Success!",
            color=discord.Color.blue()
        )
        conf_embed.add_field(name="Kicked", value=f"{member.mention} has been kicked from the server by {ctx.author.mention}", inline=False)
        conf_embed.add_field(name="Reason", value=modreason, inline=False)   
        conf_embed.set_author(name = ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
        await ctx.send(embed = conf_embed)
           
# * -------------------------------------------------------------------

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member: discord.Member, *, modreason):
        await ctx.guild.ban(member)
        conf_embed = discord.Embed(
            title=f"Success!",
            color=discord.Color.blue()
        )
        conf_embed.add_field(name="Banned", value=f"{member.mention} has been banned from the server by {ctx.author.mention}", inline=False)
        conf_embed.add_field(name="Reason", value=modreason, inline=False)   
        conf_embed.set_author(name = ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
        await ctx.send(embed = conf_embed)
           
# * -------------------------------------------------------------------
   
    @commands.command(name="unban")
    @commands.guild_only()
    @commands.has_permissions(ban_members = True)
    async def unban(self, ctx, userId):
        user = discord.Object(id = userId)
        await ctx.guild.unban(user)
        
        conf_embed = discord.Embed(
            title=f"Success!",
            color=discord.Color.blue()
        )
        conf_embed.add_field(name="Unbanned", value=f"<@{userId}> has been unbanned from the server by {ctx.author.mention}", inline=False)
        await ctx.send(embed = conf_embed)   

# * -------------------------------------------------------------------

    @commands.command()
    @commands.has_permissions(administrator = True)
    async def setmuterole(self, ctx, role: discord.Role):
        with open("mutes.json", "r") as f:
            mute_role = json.load(f)
            mute_role[str(ctx.guild.id)] = role.name
        with open("mutes.json", "w") as f:
            json.dump(mute_role, f, indent = 4)
            
        conf_embed = discord.Embed(
            title=f"Success!",
            color=discord.Color.blue()
        )
        conf_embed.add_field(name="Mute role has been set", value=f"The mute role has been changed to `{role.mention}` for this guild. All members equiped with this role will be muted!", inline=False)
        await ctx.send(embed = conf_embed)

# * -------------------------------------------------------------------

    @commands.command()
    @commands.has_permissions(manage_roles = True)
    async def mute(self, ctx, member: discord.Member):
        with open("mutes.json", "r") as f:
            role = json.load(f)
            mute_role = discord.utils.get(ctx.guild.roles, name = role[str(ctx.guild.id)])            # Getting guild roles from person that ran the command and looking for name of the role that matches the name in json file

        await member.add_roles(mute_role)
        conf_embed = discord.Embed(
            title=f"Success!",
            color=discord.Color.blue()
        )
        conf_embed.add_field(name="Muted", value=f"{member.mention} has been muted by {ctx.author.mention}.", inline=False)
        await ctx.send(embed = conf_embed)
        
# * -------------------------------------------------------------------

    @commands.command()
    @commands.has_permissions(manage_roles = True)
    async def unmute(self, ctx, member: discord.Member):
        with open("mutes.json", "r") as f:
            role = json.load(f)
            mute_role = discord.utils.get(ctx.guild.roles, name = role[str(ctx.guild.id)])            # Getting guild roles from person that ran the command and looking for name of the role that matches the name in json file

        await member.remove_roles(mute_role)
        conf_embed = discord.Embed(
            title=f"Success!",
            color=discord.Color.blue()
        )
        conf_embed.add_field(name="Unmuted", value=f"{member.mention} has been unmuted by {ctx.author.mention}.", inline=False)
        await ctx.send(embed = conf_embed)
        
# * -------------------------------------------------------------------

async def setup(bot):
    await bot.add_cog(Moderation(bot))
    