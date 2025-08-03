from telegram.ext import Updater, CallbackContext , CommandHandler
from telegram import Update
from config import TOKEN

def start(update : Update, context : CallbackContext):
    pass






updater = Updater(TOKEN)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))
updater.start_polling()
updater.idle()
