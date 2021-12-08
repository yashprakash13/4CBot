import asyncio
import re

import discord
from botutils.embeds import get_help_embed
from discord.ext.commands import Cog, command


class HelpCog(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command("help")
    async def help(self, ctx):
        async with ctx.typing():
            await asyncio.sleep(1)
        embed_help = get_help_embed()
        message = await ctx.send(embed=embed_help)
        await message.add_reaction("✅")

    # @command('about')
    # async def about(self, ctx):
    #     async with ctx.typing():
    #         await asyncio.sleep(1)
    #     embed_about = get_about_embed()
    #     message = await ctx.send(embed=embed_about)
    #     await message.add_reaction('❤️')


def setup(bot):
    bot.add_cog(HelpCog(bot))
