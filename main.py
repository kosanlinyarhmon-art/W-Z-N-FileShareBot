import os
import sys
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 
from flask import Flask
from threading import Thread

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

BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
BOT_USERNAME = os.environ.get("BOT_USERNAME")

if not BOT_TOKEN or not API_ID or not API_HASH:
    print("Error: Environment variables missing!")
    sys.exit(1)

Bot = Client(
    "File Store Bot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)

@Bot.on_message(filters.private & (filters.photo | filters.video | filters.voice | filters.document | filters.animation | filters.audio | filters.sticker))
async def hagadmansa(bot, message):
    hagadmansa = await message.reply("`Processing...`")
    media = message.photo or message.video or message.voice or message.document or message.animation or message.audio or message.sticker 
    link = f"https://t.me/{BOT_USERNAME}?start={media.file_id}"
    share = f"https://t.me/share/url?url={link}&text=Click%20on%20link%20to%20get%20the%20file%20now,%20Join%20@Hagadmansa"
    
    # ဒီနေရာမှာ ပြင်ထားပါတယ်
    await hagadmansa.edit(
        text=f"Here is your link: {link}",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('Share now', url=share)]])
    )

if __name__ == "__main__":
    keep_alive()
    Bot.run()
