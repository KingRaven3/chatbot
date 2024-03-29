from pyrogram import Client , filters
from ai import getmsg
import os

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


bot.run()

