import telegram.ext
from telegram.ext import updater

import Constents as keys
import Responses as R

print("Bot Started.....")


def start_command(update, context):
    update.message.reply_text("Hello")

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)

    update.message.reply_text(response)



def main():
    updater = telegram.ext.Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(telegram.ext.CommandHandler("start", start_command))

    dp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))

    updater.start_polling()
    updater.idle()


main()
