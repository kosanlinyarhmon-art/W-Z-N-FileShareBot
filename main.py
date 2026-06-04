import os
import sys
import asyncio
from flask import Flask
from threading import Thread
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ပြီးရင် Code ရဲ့ အောက်ဆုံးမှာ ဒီလိုလေး ပြင်ပါ:
if __name__ == "__main__":
    try:
        Thread(target=run_flask).start()
        print("Bot is starting...")
        Bot.run()
    except Exception as e:
        print(f"--- CRITICAL ERROR: {e} ---")

# Flask Setup
app = Flask(__name__)
@app.route('/')
def home():
    return "Bot is running!"

def run_flask():
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))

# Bot Configuration
BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_USERNAME = os.environ.get("BOT_USERNAME")

# Proxy setup
proxy = dict(hostname="118.107.29.235", port=1080)

Bot = Client(
    "FileStoreBot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    proxy=proxy
)

@Bot.on_message(filters.private & (filters.photo | filters.video | filters.voice | filters.document | filters.animation | filters.audio | filters.sticker))
async def hagadmansa(bot, message):
    msg = await message.reply("`Processing...`")
    media = message.photo or message.video or message.voice or message.document or message.animation or message.audio or message.sticker 
    link = f"https://t.me/{BOT_USERNAME}?start={media.file_id}"
    share = f"https://t.me/share/url?url={link}&text=Click%20on%20link%20to%20get%20the%20file%20now"
    await msg.edit(
        text=f"Here is your link: {link}",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('Share now', url=share)]])
    )

if __name__ == "__main__":
    # Flask ကို Background မှာ run
    Thread(target=run_flask).start()
    # Bot ကို run
    Bot.run()
