import telegram.ext

import Constents as keys
import Responses as R

print("Bot started...(A bot by @SanilaRanatunga)")


def start_command(update, context):
    update.message.reply_text(
        "Welcome to Useful & Powerful Chat bot🤗\nJust type random to get started✍\nHavent any idea about hove to use me🤔 type /help\nAre you need to know what's new in this version🤗🤔type What's new\n(A bot by @SanilaRanatunga)")


def help_command(update, context):
    update.message.reply_text(
        'Just send me the command that you want🙂\n/song - I will download songs for you📩\n/video - I will download youtube videos for you📩\n/torrent - I will download torrent files to you📩\n/feedback - Send me problems and errors in this bot☺\n/rules - To know the rules of this bot👽')


def song_command(update, context):
    update.message.reply_text('📨Use this telegram bot link to download songs. t.me/songdownload597_bot')


def rules_command(update, context):
    update.message.reply_text(
        "⚠Don't send emojies to this bot because you won't get a result\n⚠Just type correctly and check your spellings are correct\n⚠If this bot isn't working or not responding,just wait a moment and report that problem via /feedback\n⚠To know latest updates just send What's new")


def feedback_command(update, context):
    update.message.reply_text(
        "Are there any problems in this bot🤔 or have you any idea that should in this bot💡\nSend your problems - @SanilaRanatunga\nThanks for connecting with us🤗❤")


def video_command(update, context):
    update.message.reply_text(
        '📨Use this telegram bot link to download youtube videos. t.me/youtubevideodownloader45_bot')


def torrent_command(update, context):
    update.message.reply_text('📨Use this telegram bot to download torrent files. t.me/torrentdownloader55_bot')


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)

    update.message.reply_text(response)


def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    updater = telegram.ext.Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(telegram.ext.CommandHandler("start", start_command))
    dp.add_handler(telegram.ext.CommandHandler("help", help_command))
    dp.add_handler(telegram.ext.CommandHandler("song", song_command))
    dp.add_handler(telegram.ext.CommandHandler("video", video_command))
    dp.add_handler(telegram.ext.CommandHandler("torrent", torrent_command))
    dp.add_handler(telegram.ext.CommandHandler("feedback", feedback_command))
    dp.add_handler(telegram.ext.CommandHandler("rules", rules_command))

    dp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()
