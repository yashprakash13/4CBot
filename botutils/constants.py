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

# just a placeholder reply for the bot in case a message/embed isn't formed
BLANK_REPLY = "AVADA KEDAVRA"

# All channels and their IDs
ARTICLES_CHANNEL = 881160567950278686
ARTICLES_LINKS_CHANNEL = 881221170903531520
VIDEOS_CHANNEL = 784146876639084574
VIDEOS_LINKS_CHANNEL = 784150280970174474
GENERAL_CHANNEL = 784146201959596133

# The descriptions of all channels in the 4C server
CHANNEL_ABOUT_COG_CONTENT = {
    784382445205848106: "Here you can make respectful suggestions about the server itself.",
    881808811344683028: "This is the channel to talk about the 4C Community's website.",
    784146201959596133: "The community chat goes in here.",
    905829662062706729: "Post your short term/long term goals and achievements here.",
    900783924689666088: "You can link your Twitter spaces here.",
    881205813811761162: "If you any doubts and questions in code, post it here. Someone will help you out.",
    881160567950278686: "This is the channel to talk about creating and posting articles.",
    881221170903531520: "Here, you can post your article links. Discuss about them in the articles channel.",
    784146876639084574: "Share and discuss your video ideas here.",
    784150280970174474: "Share your YouTube video links here.",
    784374642789187604: "Put a message here if you'd like to collaborate on something, and interested members would reach out!",
    881430444049039420: "To talk about opportunities, paid collaborations and sponsored promotions",
    889226374668230717: "Post if you are ready to work as a dev, writer, etc.",
    784374776118116383: "Discuss about video gears. Folks here know their stuff!",
    881374480537120848: "Share any resources here.",
    885451366615646229: "This is the 4C Off-topic Channel. Here you can talk about... anything and everything that you want, as long it abides by the community's rules.",
    889428035424636959: "Channel for running bot commands only.",
    890040359567130656: "Talk about game development here!",
    908990638064795648: "Talk about growing your online audience here.",
    898876415049613342: "This chat is intended to share links or use the chat while in a videocall or a stream.",
}

# a flag to indicate whether to react to a message or not
REACT_OR_NOT = False
