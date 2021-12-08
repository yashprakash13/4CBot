"""
Here, the bot will handle everyone who foolishly disregard simple rules of the link channels and politely prompt them to rectify their mistakes.
"""


import re

from botutils.constants import (
    ARTICLES_CHANNEL,
    ARTICLES_LINKS_CHANNEL,
    BLANK_REPLY,
    GENERAL_CHANNEL,
    VIDEOS_CHANNEL,
    VIDEOS_LINKS_CHANNEL,
)


def handle_article_articlelinks_stupidity(message):
    all_links = re.findall(r"(https?://[^\s]+)", message)
    message_reply = BLANK_REPLY
    if len(all_links) > 0:
        message_reply = f"You have sent a link here in the discussions channel. Are you sure it doesn't belong in either <#{ARTICLES_LINKS_CHANNEL}> or <#{GENERAL_CHANNEL}>?"
    return message_reply


def handle_videos_videoslinks_stupidity(message):
    all_links = re.findall(r"(https?://[^\s]+)", message)
    message_reply = BLANK_REPLY
    if len(all_links) > 0:
        message_reply = f"You have sent a link here in the discussions channel. Are you sure it doesn't belong in either  <#{VIDEOS_LINKS_CHANNEL}> or <#{GENERAL_CHANNEL}>?"
    return message_reply
