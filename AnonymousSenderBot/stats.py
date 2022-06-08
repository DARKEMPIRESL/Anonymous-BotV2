from AnonymousSenderBot.database.users_sql import Users, num_users
from AnonymousSenderBot.database.chats_sql import num_chats
from AnonymousSenderBot.database import SESSION
from pyrogram import Client, filters
from pyrogram.types import Message
from config import configs


@Client.on_message(~filters.edited & ~filters.service, group=1)
async def users_sql(_, msg: Message):
    if msg.from_user:
        q = SESSION.query(Users).get(int(msg.from_user.id))
        if not q:
            SESSION.add(Users(msg.from_user.id))
            SESSION.commit()
        else:
            SESSION.close()


@Client.on_message(filters.user(configs.OWNER_ID) & ~filters.edited & filters.command("stats"))
async def _stats(_, msg: Message):
    users = await num_users()
    chats = await num_chats()
    await msg.reply(f"Total Users : {users} \n\nTotal Chats : {chats}", quote=True)
