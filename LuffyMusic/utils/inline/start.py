from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="💌 sᴜᴍᴍᴏɴ ᴍᴇ 💌",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="ʜᴇʟᴘ",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="sᴇᴛᴛɪɴɢs", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="💌 sᴜᴍᴍᴏɴ ᴍᴇ 💌",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="ʜᴇʟᴘ ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅs", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="♻️ sᴜᴩᴩᴏʀᴛ ♻️", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="🍁 ᴅᴇᴠᴇʟᴏᴘᴇʀ 🍁", user_id=OWNER
            )
        ],
     ]
    return buttons
