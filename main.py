import os
import asyncio
from flask import Flask
from threading import Thread
from pyrogram import Client, idle

# Flask Setup
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

# Bot Setup
BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")

Bot = Client("my_bot", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

async def main():
    await Bot.start()
    print("Bot is started!")
    await idle() # ဒီကောင်က Bot ကို အသက်ဝင်နေအောင် ထိန်းထားပေးမှာပါ

if __name__ == "__main__":
    # Flask ကို Thread နဲ့ အရင် run
    Thread(target=run_flask).start()
    
    # Bot ကို asyncio နဲ့ run
    asyncio.run(main())
