"""
Here, the bot will handle everyone who foolishly disregard simple rules of the link channels and politely prompt them to rectify their mistakes.
"""


import re

from botutils.constants import (
    ARTICLES_LINKS_CHANNEL,
    BLANK_REPLY,
    GENERAL_CHANNEL,
    REACT_OR_NOT,
    SAFE_LINKS,
    VIDEOS_LINKS_CHANNEL,
)


def handle_article_articlelinks_stupidity(message):
    message_reply = BLANK_REPLY
    if any(link in message for link in SAFE_LINKS):
        return (message_reply, REACT_OR_NOT)
    all_links = re.findall(r"(https?://[^\s]+)", message)
    if len(all_links) > 0:
        message_reply = f"You have sent a link here in the discussions channel. Are you sure it doesn't belong in either <#{ARTICLES_LINKS_CHANNEL}> or <#{GENERAL_CHANNEL}>?"
    return (message_reply, ~REACT_OR_NOT)


def handle_videos_videoslinks_stupidity(message):
    message_reply = BLANK_REPLY
    if any(link in message for link in SAFE_LINKS):
        return (message_reply, REACT_OR_NOT)
    all_links = re.findall(r"(https?://[^\s]+)", message)
    if len(all_links) > 0:
        message_reply = f"You have sent a link here in the discussions channel. Are you sure it doesn't belong in either  <#{VIDEOS_LINKS_CHANNEL}> or <#{GENERAL_CHANNEL}>?"
    return (message_reply, ~REACT_OR_NOT)


def handle_general_links_stupidity(message):
    message_reply = BLANK_REPLY
    if any(link in message for link in SAFE_LINKS):
        return (message_reply, REACT_OR_NOT)
    all_links = re.findall(r"(https?://[^\s]+)", message)
    if len(all_links) > 0:
        message_reply = f"You have sent a link here in the general chat channel. Are you sure it doesn't belong elsewhere? Your message will be deleted in 5 seconds."
    return (message_reply, REACT_OR_NOT)
