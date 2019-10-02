import logging
import re

from telegram import ParseMode
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater, CallbackContext

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


def create_scheduled_handler(schedule):
    def scheduled_handler(context: CallbackContext):
        if schedule.group:
            text = f'{schedule.group.mention_all()} {schedule.text}'
        else:
            text = schedule.text

        context.bot.send_message(schedule.chat_id, text, parse_mode=ParseMode.MARKDOWN)

    return scheduled_handler


def main():
    updater = Updater(token=config.TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start_handler))
    dispatcher.add_handler(CommandHandler('ping', ping_handler))
    dispatcher.add_handler(CommandHandler('help', help_handler))

    dispatcher.add_error_handler(error_handler)

    # Init mention group commands
    for group in config.GROUPS:
        dispatcher.add_handler(CommandHandler(
            group.commands, create_group_handler(group)))

    # Init simple answers handlers
    for answer in config.ANSWERS:
        dispatcher.add_handler(MessageHandler(
            Filters.regex(answer.regex), create_answer_handler(answer)))

    # Init scheduled messages
    for scheduled in config.SCHEDULED:
        updater.job_queue.run_daily(
            create_scheduled_handler(scheduled), scheduled.time, scheduled.days)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
