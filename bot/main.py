import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

client = discord.Client()
bot = commands.Bot(command_prefix="!")
TOKEN = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
    # Game
    # activity = discord.Game(name="Overwatch")
    activity = discord.Activity(type=discord.ActivityType.listening, name="you")
    await bot.change_presence(activity=activity)
    print(f"Logged in as {bot.user.name}({bot.user.id})")

@bot.command()
async def ping(ctx):
    await ctx.send('Pong! {0}'.format(round(bot.latency, 1)))

@bot.command()
async def queue(ctx, user: discord.User):
    await ctx.send('Successfully queued you!')

# @bot.command()
# async def DM(ctx, user: discord.User, *, message=None):
#     message = message or "This Message is sent via DM"
#     await user.send(message)

@client.event
async def on_message(self, message):
    if not message.guild:
        await message.channel.send('this is a dm')

if __name__ == "__main__":
    bot.run(TOKEN)
