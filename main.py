import asyncio
import os
from itertools import cycle

import discord
from discord.ext import commands, tasks
from discord.ext.commands import Bot
from dotenv import load_dotenv

from botutils.constants import *

TOKEN = os.environ.get("DISCORD_TOKEN")

bot = Bot(command_prefix=".", help_command=None)

load_dotenv()

STATUSES = cycle(STATUS_ACTIVITY_DICT.keys())
ACTIVITIES = cycle(STATUS_ACTIVITY_DICT.values())


@tasks.loop(seconds=1)
async def loop_bot_status():
    """
    Loop through all statuses for the bot every 13 sec
    """

    await bot.wait_until_ready()

    await bot.change_presence(activity=discord.Activity(type=next(ACTIVITIES), name=(next(STATUSES)).strip()))
    await asyncio.sleep(13)


# run the bot
# loop_bot_status.start()
# bot.load_extension("helpercogs.help_cog")
# bot.load_extension("helpercogs.channel_about_cog")
# bot.run(TOKEN)

from threading import Thread

import uvicorn
from fastapi import FastAPI

app = FastAPI()  # notice that the app instance is called `app`, this is very important.


@app.get("/")
def main():
    return "Your bot is alive!"


def run():
    uvicorn.run(app, host="0.0.0.0", port=8000)


# from flask import Flask

# app = Flask('')

# def run():
#     app.run(host="0.0.0.0", port=8080)

# def keep_alive():
#     server = Thread(target=run)
#     server.start()


def run_bot():
    t = Thread(target=run)
    t.start()


run_bot()

loop_bot_status.start()
bot.load_extension("helpercogs.help_cog")
bot.load_extension("helpercogs.channel_about_cog")
bot.run(TOKEN)
