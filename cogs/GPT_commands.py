import discord
from discord.ext import commands
import openai
from settings import DISCORD_API_TOKEN


col = discord.Color.purple()
client = openai.OpenAI(api_key=DISCORD_API_TOKEN)

class GPT_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        openai.api_key = DISCORD_API_TOKEN
                
# * -------------------------------------------------------------------

    @commands.command() 
    async def chat(self, ctx, *, message):
        
        chatstr = f"{message}"
        
        response = client.chat.completions.create(                               
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"{chatstr}"}],
            temperature=0
        )
        
        embed = discord.Embed(
            title=f"{ctx.author.display_name}: {chatstr}",
            description=response.choices[0].message.content,
            color=col
        )
        
        await ctx.send(embed=embed)
   
# * -------------------------------------------------------------------   

    @commands.command() 
    async def explain(self, ctx, *, message):
        
        chatstr = f"{message}"
        
        response = client.chat.completions.create(                               
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"Explain {chatstr}"}],
            temperature=0
        )
        
        embed = discord.Embed(
            title=f"{ctx.author.display_name}: {chatstr}",
            description=response.choices[0].message.content,
            color=col
        )
        
        await ctx.send(embed=embed)
   
# * -------------------------------------------------------------------   

    @commands.command() 
    async def generate(self, ctx, *, message):
        
        chatstr = f"{message}"
        
        response = client.images.generate(
            model="dall-e-3",
            prompt=f"{chatstr}",
            size="1024x1024",
            quality="standard",
            n=1,
        )
        
        embed = discord.Embed(
            title=f"{ctx.author.display_name}: {chatstr}",
            color=col
        )
        embed.set_image(url=response.data[0].url)
        
        await ctx.send(embed=embed)
    
# * -------------------------------------------------------------------   
    
async def setup(bot):
    await bot.add_cog(GPT_commands(bot))
    