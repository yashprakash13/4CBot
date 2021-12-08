from os import link

from discord import Colour, Embed, embeds


def get_help_embed():
    """to return help embed"""
    embed = Embed(
        title="Help",
        description=f"Some helpful information the 4C bot. For any questions, feature requests, or if you want to help with the bot maintenance, please contact <@{620092386395029565}>",  # This is me :D
        color=0xDB6F77,
    )

    embed.add_field(
        name="1. About Channel",
        value="Want to quickly know what a channel is for? Just send a ```.about``` message.",
        inline=True,
    )

    embed.add_field(
        name="2. Housekeeping functions",
        value=f"This is a feature to help moderate the articles and videos channels in the server.",
        inline=False,
    )

    # embed.footer(text=f"")

    return embed
