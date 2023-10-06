import pathlib

DISCORD_API_TOKEN = '______________'
feedback_channel = 1159938702232010762

base = pathlib.Path(__file__).parent              # gives the path of file's parent file i.e. path of project folder
cmds = base/"cogs"                          # appending commands folder project path
