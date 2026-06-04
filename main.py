import os
import sys
import logging
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from flask import Flask
from threading import Thread

# Error တွေကို Log မှာ ပြအောင် လုပ်ပေးခြင်း
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()

# Variable တွေကို စစ်ဆေးခြင်း
try:
    BOT_TOKEN = os.environ["BOT_TOKEN"]
    API_ID = int(os.environ["API_ID"])
    API_HASH = os.environ["API_HASH"]
    BOT_USERNAME = os.environ["BOT_USERNAME"]
except KeyError as e:
    logger.error(f"Missing Environment Variable: {e}")
    sys.exit(1)

Bot = Client(
    "File Store Bot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)

# ... ကျန်တဲ့ Bot Code များ ...

if __name__ == "__main__":
    keep_alive()
    logger.info("Starting Bot...")
    Bot.run()
