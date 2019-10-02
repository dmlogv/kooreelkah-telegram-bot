import logging

from telegram.ext import CommandHandler, Updater

from items.answer import init_answers
from items.group import init_groups
from items.scheduled import init_scheduled_messages

try:
    import config
except ImportError:
    raise ImportError('You must to build your own config.py based on config.default.py')

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s:%(name)s:%(levelname)s:%(message)s')


def start_handler(update, context):
    update.message.reply_text('Hi all')


def ping_handler(update, context):
    update.message.reply_text('Nope')


def help_handler(update, context):
    update.message.reply_text('Help message')


def error_handler(update, context):
    logging.error(update, context.error)


def main():
    updater = Updater(token=config.TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start_handler))
    dispatcher.add_handler(CommandHandler('ping', ping_handler))
    dispatcher.add_handler(CommandHandler('help', help_handler))

    dispatcher.add_error_handler(error_handler)

    init_groups(dispatcher, config.GROUPS)
    init_answers(dispatcher, config.ANSWERS)
    init_scheduled_messages(updater.job_queue, config.SCHEDULED)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
