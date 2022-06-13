from pyrogram import Client
from database.access import dark
from pyrogram.types import Message


async def AddUser(bot: Client, update: Message):
    if not await dark.is_user_exist(update.from_user.id):
           await dark.add_user(update.from_user.id)
