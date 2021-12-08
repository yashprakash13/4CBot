import asyncio
import os
from itertools import cycle

import discord
from discord.ext import commands, tasks
from discord.ext.commands import Bot
from dotenv import load_dotenv

from botutils.constants import *
from brain import receiver

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


@bot.event
async def on_message(message):
    """
    Command to process messages by commands as well as means other than commands
    """

    # To see if commnds need to be executed too
    await bot.process_commands(message)

    # get the message
    msg = message.content.lower()

    # Do not reply to self
    if message.author == bot.user:
        return
    # Do not reply to any other bot
    if message.author.bot:
        return

    # if it's none of the above, proceed to message handling
    msg_channel = message.channel.id
    replies_to_send, embeds_to_send = receiver.process_message(msg, msg_channel)
    if replies_to_send:
        async with message.channel.typing():
            for reply in replies_to_send:
                try:
                    await message.reply(reply, mention_author=True)
                except:
                    await message.reply(reply)


from threading import Thread

import uvicorn
from fastapi import FastAPI

app = FastAPI()  # notice that the app instance is called `app`, this is very important.


@app.get("/")
def main():
    return "Your bot is alive!"


def run():
    uvicorn.run(app, host="0.0.0.0", port=8000)


def run_bot():
    t = Thread(target=run)
    t.start()


run_bot()

loop_bot_status.start()
bot.load_extension("helpercogs.help_cog")
bot.load_extension("helpercogs.channel_about_cog")
bot.run(TOKEN)
