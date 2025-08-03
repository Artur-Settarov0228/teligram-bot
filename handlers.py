from telegram import Update
from telegram.ext import CallbackContext


def start(update : Update, context : CallbackContext):
    user = update.message.from_user
    update.message.reply_text(
        f"Assalomu aleykum botimizga xush kelibsiz! {user.full_name}.\n\n"
        "Bu bot testing uchun ishlatiladi"
    )

def help(update : Update, context : CallbackContext):
    update.message.reply_text(
        'qanday yordam kerak'
    ) 

def echo(update : Update, context : CallbackContext):
    update.message.reply_text(update.message.text) 