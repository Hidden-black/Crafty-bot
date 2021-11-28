import os
import asyncio
import aiohttp
import time
import sys
import discord
from datetime import datetime
from discord.ext import commands
import json


def get_prefix(bot, message):
    try:
        with open('prefix.json', 'r') as f:
            prefix = json.load(f)
        return prefix[str(message.guild.id)]

    except Exception as e:
        return "."

bot = commands.Bot(command_prefix= ',' , intents=discord.Intents.all(), case_insensitive=True)
bot.owner_ids = [842950909159145493, 740906193312284715]
bot.launch_time = datetime.utcnow()
bot.help_command = None

os.environ["JISHAKU_FORCE_PAGINATOR"] = "True"

extensions = [
    'jishaku',
    'cogs.mod',
    'cogs.games',
    'cogs.triggers',
    'cogs.help'
]

if __name__ == "__main__":
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'error loading {extension}', file=sys.stderr)
            print(e)


@bot.command(aliases=['egprefix'])  # COMMAND TO SET PREFIX
@commands.has_permissions(manage_channels=True)
async def prefix(ctx, prefixset):
    with open('prefix.json', 'r') as f:
        prefix = json.load(f)
    prefix[str(ctx.guild.id)] = prefixset
    with open('prefix.json', 'w') as f:
        json.dump(prefix, f, indent=4)
    await ctx.send(f"Prefix Changed To `{prefixset}`")
    



@bot.event  # activity
async def on_ready():
    # await bot.change_presence(activity=discord.Streaming(name="Subscibe To Craftymasterman", url="https://www.youtube.com/c/CraftyMasterman"))
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Craftymasterman"))
    print("-----------------------------------")
    print("Bot is ready!")


with open("./config.json") as f:
    configData = json.load(f)

Token = configData["Token"]

bot.run(Token)