from Data import Data
from pyrogram import Client, filters
from pyrogram.types import  InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto, InputTextMessageContent


# Start Message
@Client.on_message(filters.private & filters.incoming & filters.command("start"))
async def start(anonbot, msg):
    print("/start")
    user = await anonbot.get_me()
    mention = user["mention"]
    text = Data.START
    await anonbot.send_message(
        msg.chat.id,
        message.reply_photo(START_IMG,
        caption=text.format(msg.from_user.mention, mention),
        Data.START_IMG
        reply_markup=InlineKeyboardMarkup(Data.buttons),
    )
