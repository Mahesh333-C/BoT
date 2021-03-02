
from telegram.ext 
import Updater, CommandHandler, MessageHandler, Filters
try:
    from PIL import Image
except ImportError:
import Image
import pytesseract
from traceback import print_exc

def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi ' + str(update.message.from_user.full_name))


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update, context):
    """Echo the user message."""
    query = update.message.text
    update.message.reply_text("I got query : " + query)

def donate(update, context):
    update.message.reply_text("Thanks for hitting donate command!")

def convert_image(update , context):
    #print(update.message)
    filename = "test.jpg"
    file_id = update.message.photo[-1].file_id
    newFile = context.bot.get_file(file_id)
    print(update.message.photo)
    newFile.download(filename)

    update.message.reply_text("I got image :)")
     #Simple image to string
     try:
         #pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
         extrated_string = (pytesseract.image_to_string(Image.open(filename)))
     except Exception:
         print_exc()
     if extrated_string is not None:
         update.message.reply_text(extrated_string)
     else:
         update.message.reply_text("Sorry I can't able to extract text from image!:(")
    

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1694115670:AAGNrrgYozSPPGFND9VrWX2Z8Qi8Hw3GtcI", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("donate", donate))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_handler(MessageHandler(Filters.photo, convert_image))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
