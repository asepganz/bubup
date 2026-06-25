

from config import FORCE_SUB, BUTTONS_JOIN_TEXT
from pyrogram.types import InlineKeyboardButton


def start_button(client):
    if not FORCE_SUB:
        return [
            [InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close")]
        ]

    dynamic_buttons = []
    current_row = []

    for key in FORCE_SUB.keys():
        current_row.append(
            InlineKeyboardButton(
                text=f"{BUTTONS_JOIN_TEXT} {key}",
                url=getattr(client, f"invitelink{key}")
            )
        )
        # Diubah menjadi 2 agar JOIN 3 otomatis turun ke bawah
        if len(current_row) == 2:
            dynamic_buttons.append(current_row)
            current_row = []

    if current_row:
        dynamic_buttons.append(current_row)

    # gabungkan tombol dinamis dengan tombol tutup
    dynamic_buttons.append(
        [InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close")]
    )

    return dynamic_buttons


def fsub_button(client, message):
    if FORCE_SUB:
        dynamic_buttons = []
        current_row = []

        for key in FORCE_SUB.keys():
            current_row.append(
                InlineKeyboardButton(
                    text=f"{BUTTONS_JOIN_TEXT} {key}",
                    url=getattr(client, f"invitelink{key}")
                )
            )
            # Diubah menjadi 2 agar JOIN 3 otomatis turun ke bawah
            if len(current_row) == 2:
                dynamic_buttons.append(current_row)
                current_row = []

        if current_row:
            dynamic_buttons.append(current_row)

        try:
            dynamic_buttons.append([
                InlineKeyboardButton(
                    text="ᴄᴏʙᴀ ʟᴀɢɪ",
                    url=f"https://t.me/{client.username}?start={message.command[1]}"
                )
            ])
        except IndexError:
            pass

        return dynamic_buttons
        
