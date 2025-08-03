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

def echo_photo(update : Update, context : CallbackContext):
    update.message.reply_photo(update.message.photo[-1].file_id)


def echo_video(update : Update, context : CallbackContext):
    update.message.reply_video(update.message.video.file_id)


def echo_audio(update : Update, context : CallbackContext):
    update.message.reply_audio(update.message.audio.file_id)


def echo_sticker(update : Update, context : CallbackContext):
    update.message.reply_sticker(update.message.sticker.file_id)



def echo_voice(update : Update, context : CallbackContext):
    update.message.reply_voice(update.message.voice.file_id)


def echo_doc(update : Update , context : CallbackContext):
    update.message.reply_document(update.message.document.file_id)

def echo_Contact(update: Update, context: CallbackContext):
    contact = update.message.contact
    update.message.reply_contact(
        phone_number=contact.phone_number,
        first_name=contact.first_name,
        last_name=contact.last_name if contact.last_name else ""
    )


def echo_location(update: Update, context: CallbackContext):
    location = update.message.location
    update.message.reply_location(latitude=location.latitude, longitude=location.longitude)


def echo_video_note(update : Update, context : CallbackContext):
    pass
    
