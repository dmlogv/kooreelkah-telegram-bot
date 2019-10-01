import logging
import re

from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

try:
    import config
except ImportError:
    raise ImportError('You must to build your own config.py based on config.default.py')


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s:%(name)s:%(levelname)s:%(message)s')


def start(update, context):
    update.message.reply_text('Hi all')


def ping(update, context):
    update.message.reply_text('Nope')


def help(update, context):
    update.message.reply_text('Help message')


def error(update, context):
    logging.error(update, context.error)


def main():
    updater = Updater(token=config.TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('ping', ping))
    dispatcher.add_handler(CommandHandler('help', help))

    dispatcher.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
