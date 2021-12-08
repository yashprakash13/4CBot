from botutils.constants import ARTICLES_CHANNEL, BLANK_REPLY, VIDEOS_CHANNEL

from .wrong_channel_brain import wrong_channel_brain


def process_message(msg, msg_channel_id):
    all_replies, all_embeds = [], []

    # if articles or videos channels are in question respectively
    if msg_channel_id == ARTICLES_CHANNEL:
        msg_reply = wrong_channel_brain.handle_article_articlelinks_stupidity(msg)
        if msg_reply[0] != BLANK_REPLY:  # check the message content only
            all_replies.append(msg_reply)
    elif msg_channel_id == VIDEOS_CHANNEL:
        msg_reply = wrong_channel_brain.handle_videos_videoslinks_stupidity(msg)
        if msg_reply != BLANK_REPLY:  # check the message content only
            all_replies.append(msg_reply)

    return all_replies, all_embeds
