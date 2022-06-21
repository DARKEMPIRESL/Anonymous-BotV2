from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup


# Copy Message
@Client.on_message(
    filters.private & ~filters.command(["start", "about", "help", "stats", "id"])
)
async def copy(_, msg):
    if msg.caption:
        await msg.copy(msg.chat.id, reply_markup=InlineKeyboardMarkup([Data.add_button,Data.remove_button]), disable_notification=True, reply_to_message_id=msg.message_id)
    else:
        await msg.copy(msg.chat.id, reply_markup=([Data.add_button]))
