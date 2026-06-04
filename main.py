import os
import asyncio
from pyrogram import Client, filters

# Bot Configuration
BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_USERNAME = os.environ.get("BOT_USERNAME")

# Proxy setup (အကယ်၍ ဒီတစ်ခုနဲ့မရရင် နောက်တစ်ခုပြောင်းပါ)
proxy = dict(hostname="118.107.29.235", port=1080)

Bot = Client(
    "FileStoreBot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    proxy=proxy
)

@Bot.on_message(filters.private & filters.media)
async def hagadmansa(bot, message):
    msg = await message.reply("`Processing...`")
    # media file_id ကိုယူခြင်း
    media = message.photo or message.video or message.document
    link = f"https://t.me/{BOT_USERNAME}?start={media.file_id}"
    await msg.edit(f"Here is your link: {link}")

if __name__ == "__main__":
    print("Bot is starting...")
    Bot.run()
