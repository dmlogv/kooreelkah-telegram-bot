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


def create_group_handler(group):
    def group_handler(update, context):
        mention = group.mention_all()
        text = ' '.join(context.args)

        update.message.reply_markdown(
            f'{mention} {text}',
            quote=False,
            forward_from_message_id=update.message.forward_from_message_id)

        if group.remove_command_message:
            update.message.delete()

    return group_handler


def create_answer_handler(answer):
    def answer_handler(update, context):
        update.message.reply_markdown(answer.text)

    return answer_handler


def main():
    updater = Updater(token=config.TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('ping', ping))
    dispatcher.add_handler(CommandHandler('help', help))

    dispatcher.add_error_handler(error)

    # Init mention group commands
    for group in config.GROUPS:
        dispatcher.add_handler(CommandHandler(
            group.commands, create_group_handler(group)))

    # Init simple answers handlers
    for answer in config.ANSWERS:
        dispatcher.add_handler(MessageHandler(
            Filters.regex(answer.regex), create_answer_handler(answer)))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
