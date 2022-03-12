import asyncio

import discord
from botutils.constants import CHANNEL_ABOUT_COG_CONTENT
from discord.ext.commands import Cog, command


class ChannelAbout(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command("about")
    async def help(self, ctx):
        async with ctx.typing():
            await asyncio.sleep(1)
        channel_sent_in = ctx.message.channel.id
        try:
            channel_desc_to_send = CHANNEL_ABOUT_COG_CONTENT[channel_sent_in]
            message = await ctx.send(str(channel_desc_to_send))
            await message.add_reaction("😎")
        except:
            await ctx.send("Sorry, no **about** info set for this channel yet.")


def setup(bot):
    bot.add_cog(ChannelAbout(bot))
