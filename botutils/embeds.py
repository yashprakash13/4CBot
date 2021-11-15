from os import link

from discord import Colour, Embed, embeds


def get_help_embed():
    """to return help embed"""
    embed = Embed(title="Help", description="How to use the 4C bot", color=0xDB6F77)

    embed.add_field(name="Under", value="Construction 🛠", inline=False)

    return embed
