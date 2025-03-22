import discord
from discord.ext import tasks, commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)



@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    
@bot.command()
async def start(ctx):
    print('Starting...')
    send_link.start(ctx)

@tasks.loop(hours=24)
async def send_link(ctx):
    await ctx.send("[Do the daily LeetCode challenge!](https://leetcode.com/problemset/)")

    

bot.run(TOKEN)
