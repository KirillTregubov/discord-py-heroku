import os
import discord
from discord.ext import commands

client = discord.Client()
bot = commands.Bot(command_prefix="!")
TOKEN = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")

@bot.command()
async def ping(ctx):
    await ctx.send('Pong! {0}'.format(round(bot.latency, 1)))

@client.event
async def on_message(message):
    if isinstance(message.channel, discord.channel.DMChannel) and message.author != client.user:
        await message.channel.send('This is a DM')

if __name__ == "__main__":
    bot.run(TOKEN)
