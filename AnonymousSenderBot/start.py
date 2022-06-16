from Data import Data
from pyrogram import Client, filters
from pyrogram.types import  InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto, InputTextMessageContent


# Start Message
@Client.on_message(filters.private & filters.incoming & filters.command("start"))
async def start(anonbot, msg):
    print("/start")
    user = await anonbot.get_me()
    text = Data.START
    reply_markup=Data.buttons
    START_IMG = "https://telegra.ph/file/89662416f1623875c1a03.jpg"
    
    await anonbot.reply_photo(
        START_IMG,
        caption=text.format(msg.from_user.mention, mention),
        reply_markup=reply_markup
    )
