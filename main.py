import settings
import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)


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

@bot.event                                   # Bot decorator telling it is an event 
async def on_ready():
    print(bot.user)
    print(bot.user.id)
    print("____________________________________________________________")
    
    for cmd_file in settings.cmds.glob("*.py"):                                   # yields all existing files of specified type
        if cmd_file != "__init__.py":
            await bot.load_extension(f"cogs.{cmd_file.stem}")                      # .stem provides file name without extension

# * -------------------------------------------------------------------   

# @bot.command (
#     aliases = ['p'],                           
#     help = "This is help",                    # Shows on help menu
#     description = "This is Description",      # Shows on command description menu title
#     brief = "This is brief",                  # Shows on command description menu
#     enabled = True                            # Tells if the command is enabled or not
# )
# async def ping(ctx):                         # ctx refers to the context like message, channel etc..
#     await ctx.send("PONG")

# * -------------------------------------------------------------------

if __name__ == "__main__":
    bot.run(settings.DISCORD_API_TOKEN) 
 