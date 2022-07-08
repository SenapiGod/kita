from YorForger import dispatcher
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, ParseMode

from telegram.ext import (
    CallbackContext,
    CommandHandler,
)

PHOTO = "https://telegra.ph/file/50fa58933b46c16b3df61.mp4 "

def alive(update: Update, context: CallbackContext):
    TEXT = f"I Am ITACHI UCHIHA !\n\nI Work Under - **[999 Gang 亗](https://t.me/fed999wrld)** \n\n⏺I'm working properly "


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
