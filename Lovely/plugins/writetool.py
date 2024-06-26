import requests
import config

from pyrogram import filters
from pyrogram.types import *

from Lovely import lovely

@lovely.on_message(filters.me & filters.command("write", prefixes=config.HANDLER))
async def handwriting(_, message):
    if len(message.command) < 2:
        return await message.reply_text("» Give some text to write master...")
    m = await message.reply_text("» I writing please wait master...")
    name = (
        message.text.split(None, 1)[1]
        if len(message.command) < 3
        else message.text.split(None, 1)[1].replace(" ", "%20")
    )
    API = "https://apis.xditya.me/write?text=" + name
    url = requests.get(API).url
    await m.edit("» Uploading...")
    await m.delete()
    me = await lovely.get_me()
    await message.reply_photo(url)
