#    Copyright (C) 2021 - Avishkar Patil | @AvishkarPatil


import os
import sys
import time
import logging
import pyrogram
import aiohttp
import asyncio
import requests
import aiofiles
from random import randint
from progress import progress
from config import Config
from pyrogram.errors import UserNotParticipant, UserBannedInChannel
from pyrogram import Client, filters, idle
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, InlineQuery, InputTextMessageContent


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

DOWNLOAD = "./"

# vars
APP_ID = Config.APP_ID
API_HASH = Config.API_HASH
BOT_TOKEN = Config.BOT_TOKEN

   
bot = Client(
    "AnonFilesBot",
    api_id=APP_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN)


START_TEXT = """
__Hᴇʟʟᴏ Dᴇᴀʀ I'ᴍ__ **AɴᴏɴFɪʟᴇsBᴏᴛ** 😎 \n\n__I Cᴀɴ Uᴘʟᴏᴀᴅ Fɪʟᴇs Tᴇʟᴇɢʀᴀ Tᴏ AɴᴏɴFɪʟᴇs__\n\n__MᴀɪɴTᴀɪɴᴇᴅ Bʏ__ :** @Benwolf24**
"""
HELP_TEXT = """
**AɴᴏɴFɪʟᴇsBᴏᴛ Hᴇʟᴘ**\n\n__Sᴇɴᴅ ᴍᴇ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇᴅɪᴀ ғɪʟᴇ, I'ʟʟ ᴜᴘʟᴏᴀᴅ ɪᴛ ᴛᴏ ᴀɴᴏɴғɪʟᴇs.ᴄᴏᴍ ᴀɴᴅ ɢɪᴠᴇ ʏᴏᴜ ᴅɪʀᴇᴄᴛ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ__\n\n__MᴀɪɴTᴀɪɴᴇᴅ Bʏ__ :** @Rex_Botz**
"""
ABOUT_TEXT = """
╭────[⚡ ᴀʙᴏᴜᴛ ⚡]───⍟
│
├<b>🤖 𝙱𝚘𝚝 𝙽𝚊𝚖𝚎 : <a href='https://t.me/AnonFilesRexBot'>ᴀɴᴏɴғɪʟᴇs-ᴜᴘʟ</a></b>
│
├<b>📢 𝙲𝚑𝚊𝚗𝚗𝚎𝚕  : <a href='https://t.me/Rex_Botz'>ᴊᴏɪɴ</a></b>
│
├<b>👥 𝚅𝚎𝚛𝚜𝚒𝚘𝚗  : <a href='https://t.me/Rex_Bots_Support'>0.9.2ʙᴇᴛᴀ</a></b>
│
├<b>💢 𝚂𝚘𝚞𝚛𝚌𝚎   : <a href='https://github.com/REX-BOTZ/'>ᴅᴇᴘʟᴏʏ</a></b>
│
├<b>🌐 𝚂𝚎𝚛𝚟𝚎𝚛   : <a href='https://heroku.com'>ʜᴇʀᴏᴋᴜ</a></b>
│
├<b>📕 𝙻𝚒𝚋𝚛𝚊𝚛𝚢  : <a href='https://github.com/pyrogram'>ᴘʀɢ1.2.8</a></b>
│
├<b>㊙ 𝙻𝚊𝚗𝚐𝚞𝚊𝚐𝚎 : <a href='https://www.python.org'>ᴘʏ3.9.4</a></b>
│
├<b>👨‍💻 𝙳𝚎𝚟      : <a href='https://t.me/BENWOLF24'>ᴡᴏʟғ24</a></b>
│
├<b>🚸 𝙿𝚘𝚠𝚎𝚛𝚎𝚍  : <a href='https://t.me/FluxPlay'>ғʟᴜxᴘʟᴀʏ</a></b>
│
╰──────[ᴛʜᴀɴᴋs 😊]───⍟"""

START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('About', callback_data='about'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('About', callback_data='about'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )


@bot.on_callback_query()
async def cb_data(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT,
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            disable_web_page_preview=True,
            reply_markup=ABOUT_BUTTONS
        )
    else:
        await update.message.delete()
        
        
@bot.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    text = START_TEXT
    reply_markup = START_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

      
@bot.on_message(filters.media & filters.private)
async def upload(client, message):
    if Config.UPDATES_CHANNEL is not None:
        try:
            user = await client.get_chat_member(Config.UPDATES_CHANNEL, message.chat.id)
            if user.status == "kicked":
                await client.send_message(
                    chat_id=message.chat.id,
                    text="**Sᴏʀʀʏ, Yᴏᴜ ᴀʀᴇ Bᴀɴɴᴇᴅ ᴛᴏ ᴜsᴇ ᴍᴇ! Cᴏɴᴛᴀᴄᴛ** [Dᴇᴠᴇʟᴏᴘᴇʀ](https://telegram.me/Benwolf24).",
                    parse_mode="markdown",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await client.send_message(
                chat_id=message.chat.id,
                text="**Pʟᴇᴀsᴇ Jᴏɪɴ Mʏ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ Tᴏ Usᴇ Mᴇ 🏃‍♂**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Jᴏɪɴ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ", url=f"https://t.me/{Config.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await client.send_message(
                chat_id=message.chat.id,
                text="**Sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ Wʀᴏɴɢ! Cᴏɴᴛᴀᴄᴛ ᴍʏ** [ʀᴇx sᴜᴘᴘᴏʀᴛ](https://telegram.me/Rex_Bots_Support).",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
    m = await message.reply("**Dᴏᴡɴʟᴏᴀᴅɪɴɢ Yᴏᴜʀ FIʟᴇs Tᴏ Mʏ Sᴇʀᴠᴇʀ ....** 😈")
    now = time.time()
    sed = await bot.download_media(
                message, DOWNLOAD,
          progress=progress,
          progress_args=(
            "**Uᴘʟᴏᴀᴅ Pʀᴏᴄᴇss Sᴛᴀʀᴇᴅ Wᴀɪᴛ ᴀɴᴅ Wᴀᴛᴄʜ Mᴀɢɪᴄ**\n**Iᴛs Tᴀᴋᴇ ᴛɪᴍᴇ Aᴄᴄᴏʀᴅɪɴɢ Yᴏᴜʀ Fɪʟᴇs Sɪᴢᴇ** \n\n**ᴇᴛᴀ:** ", 
            m,
            now
            )
        )
    try:
        files = {'file': open(sed, 'rb')}
        await m.edit("**Uᴘʟᴏᴀᴅɪɴɢ ᴛᴏ AɴᴏɴFIʟᴇs Sᴇʀᴠᴇʀ Pʟᴇᴀsᴇ Wᴀɪᴛ**")
        callapi = requests.post("https://api.anonfiles.com/upload", files=files)
        text = callapi.json()
        output = f"""
<u>**Fɪʟᴇ Uᴘʟᴏᴀᴅᴇᴅ Tᴏ AɴᴏɴFɪʟᴇs**</u>

**📂 Fɪʟᴇ Nᴀᴍᴇ:** {text['data']['file']['metadata']['name']}

**📦 Fɪʟᴇ Sɪᴢᴇ:** {text['data']['file']['metadata']['size']['readable']}

**📥Dᴏᴡɴʟᴏᴀᴅ Lɪɴᴋ:** `{text['data']['file']['url']['full']}`

🔅__MᴀɪɴTᴀɪɴᴇᴅ Bʏ__ :** @Rex_Botz **"""
        btn = InlineKeyboardMarkup(
                                [[InlineKeyboardButton("Dᴏᴡɴʟᴏᴀᴅ Fɪʟᴇ", url=f"{text['data']['file']['url']['full']}")]])
        await m.edit(output, reply_markup=btn)
        os.remove(sed)
    except Exception:
        await m.edit("__Pʀᴏᴄᴇss Fᴀɪʟᴇᴅ, Mᴀʏʙᴇ Tɪᴍᴇ Oᴜᴛ Dᴜᴇ Tᴏ Lᴀʀɢᴇ Fɪʟᴇ Sɪᴢᴇ!__")
        return
      
@bot.on_message(filters.regex(pattern="https://cdn-") & filters.private & ~filters.edited)
async def url(client, message):
    msg = await message.reply("__Cʜᴇᴄᴋɪɴɢ Uʀʟ...__")
    lenk = message.text
    cap = "© @AvishkarPatil"
    thumb = "./thumb.jpg"
    try:
         await msg.edit("**Bɪɢ Fɪʟᴇs Wɪʟʟ Tᴀᴋᴇ Mᴏʀᴇ Tɪᴍᴇ, Dᴏɴ'ᴛ Pᴀɴɪᴄ!**")
         filename = await download(lenk)
         await msg.edit("Uploading File To Telegram...")
         await message.reply_document(filename, caption=cap, thumb=thumb)
         await msg.delete()
         os.remove(filename)
    except Exception:
        await msg.edit("__Pʀᴏᴄᴇss Fᴀɪʟᴇᴅ, Mᴀʏʙᴇ Tɪᴍᴇ Oᴜᴛ Dᴜᴇ Tᴏ Lᴀʀɢᴇ Fɪʟᴇ Sɪᴢᴇ!__")
        
async def download(url):
    ext = url.split(".")[-1]
    filename = str(randint(1000, 9999)) + "." + ext
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                f = await aiofiles.open(filename, mode='wb')
                await f.write(await resp.read())
                await f.close()
    return filename
        
        
bot.start()
print("AnonFilesBot Is Started!,  if Have Any Problems contact @Rex_Bots_Support")
idle()
