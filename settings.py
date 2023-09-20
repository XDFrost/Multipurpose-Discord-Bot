import pathlib

DISCORD_API_TOKEN = '____________'

base = pathlib.Path(__file__).parent              # gives the path of file's parent file i.e. path of project folder
cmds = base/"cogs"                          # appending commands folder project path
