from telegram.ext.jobqueue import Days


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
