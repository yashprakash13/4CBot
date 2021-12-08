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

    # get the author
    author = message.author

    # Do not reply to self
    if message.author == bot.user:
        return
    # Do not reply to any other bot
    if message.author.bot:
        return

    # if it's none of the above, proceed to message handling
    msg_channel = message.channel.id
    channel = message.channel
    replies_to_send, embeds_to_send = receiver.process_message(msg, msg_channel)
    if replies_to_send:
        async with message.channel.typing():
            for reply in replies_to_send:
                reply_text_to_send, reply_reaction = reply[0], reply[1]
                if reply_reaction:  # if we need a reaction as a 👍
                    try:
                        reply_text_to_send = (
                            reply_text_to_send
                            + " React with a 👍 so that I can remove it from here and automatically post it for you in the correct channel."
                        )
                        await message.reply(reply_text_to_send, mention_author=True)

                        def check(reaction, user):
                            return user == message.author and str(reaction.emoji) == "👍"

                        try:
                            reaction, user = await bot.wait_for("reaction_add", timeout=30.0, check=check)
                        except asyncio.TimeoutError:
                            pass
                        else:
                            # thumbs up was reacted, so remove this message from here and move it to the appropriate channel
                            await message.delete()  # delete the original message
                            # check which channel it was originally sent in and do the appropriate action
                            if msg_channel == ARTICLES_CHANNEL:
                                articles_links_channel = bot.get_channel(ARTICLES_LINKS_CHANNEL)
                                await articles_links_channel.send(f"An article from {author.mention}: {msg}")
                            elif msg_channel == VIDEOS_CHANNEL:
                                articles_links_channel = bot.get_channel(VIDEOS_LINKS_CHANNEL)
                                await articles_links_channel.send(f"A video from {author.mention}: {msg}")
                            await channel.send("Alright, done.")

                    except:  # if no reaction was added, do nothing.
                        pass


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
