from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hi,\n\nWelcome to {}  \n\n I am **πππ₯π ππ‘π’π‘π¬π π’π¨π¦ ππ’π§.**\n
Just Forward me Some messages or
media and I will **Anonymize** that !!
Please Subscribe Our [Chanel](https://t.me/SLBotOfficial) ππ°
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
    home_button = [[InlineKeyboardButton(text="ποΈ Return Home ποΈ", callback_data="home")]]

    # Remove Caption Button
    remove_button = [InlineKeyboardButton("οΏ½ Remove Caption οΏ½", callback_data="remove")]

    # Add caption button
    add_button = [InlineKeyboardButton("π¬ Re-Add Caption π¬", callback_data="add")]

    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("βΎοΈ About The Bot βΎοΈ", callback_data="about")
        ],
        [InlineKeyboardButton("β₯ More Amazing bots β₯", url="https://t.me/SLBotOfficial/28")],
        [InlineKeyboardButton("π« Support Group π«", url="https://t.me/SLBotsChat")],
    ]

