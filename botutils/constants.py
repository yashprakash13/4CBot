import os

import discord
from dotenv import load_dotenv

load_dotenv()

STATUS_ACTIVITY_DICT = {
    ".help": discord.ActivityType.listening,
    "I am the extraordinary 4C Bot!": discord.ActivityType.playing,
    # "You wish you had a mind like me, don't you?": discord.ActivityType.playing,
    # "It's OK. You're only human, after all.": discord.ActivityType.playing,
}
