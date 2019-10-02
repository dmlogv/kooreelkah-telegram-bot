from telegram import ParseMode
from telegram.ext import CallbackContext
from telegram.ext.jobqueue import Days


def init_scheduled_messages(job_queue, scheduled):
    for scheduled in scheduled:
        job_queue.run_daily(
            create_scheduled_handler(scheduled), scheduled.time, scheduled.days)


def create_scheduled_handler(schedule):
    def scheduled_handler(context: CallbackContext):
        if schedule.group:
            text = f'{schedule.group.mention_all()} {schedule.text}'
        else:
            text = schedule.text

        context.bot.send_message(schedule.chat_id, text, parse_mode=ParseMode.MARKDOWN)

    return scheduled_handler


class ScheduledMessage:
    """Send message to specific chat by a schedule

    Args:
        chat_id: Specific chat.
        text: Text you want to send.
        time (datetime.time): Time to send message.
        days (tuple[int], int): Days of week.
            Use telegram.ext.jobqueue.Days
        group (Group): mention group
    """
    def __init__(self, chat_id, text, time, days=Days.EVERY_DAY, group=None):
        self.chat_id = chat_id
        self.text = text
        self.time = time
        self.days = days if type(days) == tuple else (days,)
        self.group = group
