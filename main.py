from telegram.ext import Updater, CallbackContext , CommandHandler, MessageHandler , Filters
from config import TOKEN
from handlers import start, help, echo



def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
#Command handler
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', help))


#Message handler

    dispatcher.add_handler(MessageHandler(Filters.text, echo))

    updater.start_polling()
    updater.idle()
if __name__ == '__main__':
    main()