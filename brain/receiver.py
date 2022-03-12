from botutils.constants import (
    ARTICLES_CHANNEL,
    BLANK_REPLY,
    GENERAL_CHANNEL,
    VIDEOS_CHANNEL,
)

from .wrong_channel_brain import wrong_channel_brain


def process_message(msg, msg_channel_id):
    all_replies, all_embeds = [], []

    # if articles or videos channels are in question respectively
    if msg_channel_id == ARTICLES_CHANNEL:
        msg_reply = wrong_channel_brain.handle_article_articlelinks_stupidity(msg)
        if BLANK_REPLY not in msg_reply[0]:  # check the message content only
            all_replies.append(msg_reply)
    elif msg_channel_id == VIDEOS_CHANNEL:
        msg_reply = wrong_channel_brain.handle_videos_videoslinks_stupidity(msg)
        if BLANK_REPLY not in msg_reply[0]:  # check the message content only
            all_replies.append(msg_reply)
    elif msg_channel_id == GENERAL_CHANNEL:
        msg_reply = wrong_channel_brain.handle_general_links_stupidity(msg)
        if BLANK_REPLY not in msg_reply[0]:  # check the message content only
            all_replies.append(msg_reply)
    else:
        pass

    return all_replies, all_embeds
