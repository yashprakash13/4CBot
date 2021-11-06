import asyncio
import os
from itertools import cycle

import discord
from discord.ext import commands, tasks
from discord.ext.commands import Bot
from dotenv import load_dotenv

from botutils.constants import *

TOKEN = os.environ.get("DISCORD_TOKEN")

bot = Bot(command_prefix=".")

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
loop_bot_status.start()
bot.run(TOKEN)
