from YorForger import dispatcher
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, ParseMode

from telegram.ext import (
    CallbackContext,
    CommandHandler,
)

PHOTO = "https://telegra.ph/file/976a903c3c286536ec646.jpg"

def alive(update: Update, context: CallbackContext):
    TEXT = f"ʜɪ, ɪ'ᴍ ɪᴛᴀᴄʜɪ ᴜᴄʜɪʜᴀ!\n\nɪ ᴡᴏʀᴋ ᴜɴᴅᴇʀ- **[999 Gang 亗](https://t.me/fed999wrld)** \n\nɪ'ᴍ ᴡᴏʀᴋɪɴɢ ᴘʀᴏᴘᴇʀʟʏ"


    update.effective_message.reply_photo(
        PHOTO, caption= TEXT,
        parse_mode=ParseMode.MARKDOWN,

            reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton(text="【Support】", url="https://t.me/fed999wrld"),
                InlineKeyboardButton(text="【Updates】", url="https://t.me/itachixobot_support")
                ],
                [InlineKeyboardButton(text="【999 Gang 亗】", url="https://t.me/fed999wrld")]
            ]
        ),
    )

void_handler = CommandHandler("alive", alive, run_async = True)
dispatcher.add_handler(void_handler)


__help__ = """ 
❂ /alive: To check if bot is alive or not."""
   
__mod_name__ = "Alive"
