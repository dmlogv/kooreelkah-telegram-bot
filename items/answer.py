import random
import re

from telegram.ext import MessageHandler, Filters


def init_answers(dispatcher, answers):
    for answer in answers:
        dispatcher.add_handler(MessageHandler(
            Filters.regex(answer.regex), create_answer_handler(answer)))


def create_answer_handler(answer):
    def answer_handler(update, _):
        update.message.reply_markdown(answer.text)

    return answer_handler


class Answer:
    """Simple answer on user messages, matching with a regular expression"""
    def __init__(self, regex, text, flags=re.IGNORECASE):
        self.regex = re.compile(regex, flags=flags)
        self.text = str(text)


class AlternativeString:
    """Choose random string

    Examples:
        > alt = AlternativeString('Hi!', 'Hello!', 'How are you?')
        > print(alt)
        Hello!
        > print(alt)
        Hi!
    """
    def __init__(self, *s):
        self.strings = s

    def __str__(self):
        return random.choice(self.strings)
