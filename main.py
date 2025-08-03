from telegram.ext import Updater, CallbackContext , CommandHandler, MessageHandler , Filters
from config import TOKEN
from handlers import (start, help, echo, echo_audio,
                      echo_photo, echo_sticker, echo_video,
                      echo_voice, echo_Contact,echo_doc,
                      echo_location
)



def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
#Command handler
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', help))


#Message handler

    dispatcher.add_handler(MessageHandler(Filters.text, echo))
    dispatcher.add_handler(MessageHandler(Filters.photo, echo_photo))
    dispatcher.add_handler(MessageHandler(Filters.audio , echo_audio))
    dispatcher.add_handler(MessageHandler(Filters.sticker, echo_sticker))
    dispatcher.add_handler(MessageHandler(Filters.voice, echo_voice))
    dispatcher.add_handler(MessageHandler(Filters.video, echo_video))
    dispatcher.add_handler(MessageHandler(Filters.contact, echo_Contact))
    dispatcher.add_handler(MessageHandler(Filters.document,echo_doc))
    dispatcher.add_handler(MessageHandler(Filters.location, echo_location))
    


    print(" Multi-Echo bot ishga tushdi...")


    updater.start_polling()
    updater.idle()
if __name__ == '__main__':
    main()