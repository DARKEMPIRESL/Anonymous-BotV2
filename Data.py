from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hi,\n\nWelcome to {}  \n\n I am **𝗗𝗔𝗥𝗞 𝗔𝗡𝗢𝗡𝗬𝗠𝗢𝗨𝗦 𝗕𝗢𝗧.**\n
Just Forward me Some messages or
media and I will **Anonymize** that !!
Please Subscribe Our [Chanel](https://t.me/SLBotOfficial) 😎🔰
"""

    # About Message
    ABOUT = """
**About This Bot** 

Bot created by @SLBotOfficial

Source Code : [Click Here](https://github.com/DARKEMPIRESL/Anonymous-BotV2)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @ImDark_Empire
    """

    # Home Button
    home_button = [[InlineKeyboardButton(text="🏛️ Return Home 🏛️", callback_data="home")]]

    # Remove Caption Button
    remove_button = [InlineKeyboardButton("� Remove Caption �", callback_data="remove")]

    # Add caption button
    add_button = [InlineKeyboardButton("💬 Re-Add Caption 💬", callback_data="add")]

    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("♾️ About The Bot ♾️", callback_data="about")
        ],
        [InlineKeyboardButton("♥ More Amazing bots ♥", url="https://t.me/SLBotOfficial/28")],
        [InlineKeyboardButton("🛫 Support Group 🛫", url="https://t.me/SLBotsChat")],
    ]

