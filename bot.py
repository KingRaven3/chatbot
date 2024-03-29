from pyrogram import Client , filters
from ai import getmsg , getpeasant
import os
import time

bot =  Client(
    "ryu",
    api_id=6,
    api_hash="eb06d4abfb49dc3eeb1aeb98ae0f581e",
    bot_token=os.environ['BOT_TOKEN'],
)

@bot.on_message(filters.regex("ryu") & filters.user(5704299476))
def ryu(_,m):
    prompt = m.text
    reply = getmsg(prompt)
    m.reply(reply)

@bot.on_message(filters.text)
def pes(_,m):
    if not m.from_user.id == 5704299476:
        prompt = m.text
        reply = getpeasant(prompt)
        m.reply(reply)


bot.run()

