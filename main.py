import settings
import discord
from discord.ext import commands
import json

intents = discord.Intents.all()

def get_server_prefix(bot, message):
        with open("cogs/json/prefixes.json", "r") as f:
            prefix = json.load(f)
        return prefix[str(message.guild.id)]

bot = commands.Bot(command_prefix=get_server_prefix, intents=intents)


# * -------------------------------------------------------------------
# * -------------------------------------------------------------------


# Handling error            
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):                                # isinstance checks if the error is caused by the provided reason or not
        await ctx.send(f"```Error: Arguments are not provided \n\nFor more info on a specific command, use {'*help*'} command```")
    else:
        await ctx.send(f"```Error occured during execution\n\nFor more info on a specific command, use {'*help*'} command```")
        raise error


# * -------------------------------------------------------------------
# * -------------------------------------------------------------------


@bot.event                                   # Bot decorator telling it is an event 
async def on_ready():
    print(bot.user)
    print(bot.user.id)
    print("____________________________________________________________")
    
    for cmd_file in settings.cmds.glob("*.py"):                                   # yields all existing files of specified type
        if cmd_file != "__init__.py":
            await bot.load_extension(f"cogs.{cmd_file.stem}")                      # .stem provides file name without extension


# * -------------------------------------------------------------------   
# * -------------------------------------------------------------------   


    @bot.event
    async def on_guild_join(guild):
# * -------------------------------------------------------------------   
        with open("cogs/json/prefixes.json", "r") as f:
            prefix = json.load(f)
        prefix[str(guild.id)] = "!"
        with open("prefixes.json", "w") as f:
            json.dump(prefix, f, indent = 4)
# * -------------------------------------------------------------------   
        with open("cogs/json/mutes.json", "r") as f:
            mute_role = json.load(f)
            mute_role[str(guild.id)] = None
        with open("cogs/json/mutes.json", "w") as f:
            json.dump(mute_role, f, indent = 4)
            
            
# * -------------------------------------------------------- -----------
# * -------------------------------------------------------------------


    @bot.event
    async def on_guild_remove(guild):
# * -------------------------------------------------------------------  
        with open("cogs/json/prefixes.json", "r") as f:
            prefix = json.load(f)
        prefix.pop(str(guild.id))
        with open("cogs/json/prefixes.json", "w") as f:
            json.dump(prefix, f, indent = 4)
# * -------------------------------------------------------------------   
        with open("cogs/json/mutes.json", "r") as f:
            mute_role = json.load(f)
            mute_role.pop(str(guild.id))
        with open("cogs/json/mutes.json", "w") as f:
            json.dump(mute_role, f, indent = 4)
            
            
# * -------------------------------------------------------------------
# * -------------------------------------------------------------------

if __name__ == "__main__":
    bot.run(settings.DISCORD_API_TOKEN) 
 