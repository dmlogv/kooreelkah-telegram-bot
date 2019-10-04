"""
kooreelkah-telegram-bot uses simple py file for the configuration.

Be careful.

Very.
"""
from datetime import time

from telegram.ext.jobqueue import Days

from items import AlternativeString, Answer, Member, Group, ScheduledMessage


# Telegram Bot Token. Ask @BotFather if you have any questions.
TOKEN = ''

# Id of the main chat (for boring daily routines)
CHAT = 0


# Explicitly create chat members for an interaction with them.
# Use charactonyms! (And see config.example.py)
admin = Member()

MEMBERS = []


# Create some groups for your members
all = Group()
admins = Group()

# Don't forget to add it to GROUPS list
GROUPS = [all, admins]


# Simple answers to react on user messages
ANSWERS = [Answer(), Answer(None, AlternativeString())]


# Scheduled messages
SCHEDULED = [ScheduledMessage(CHAT)]
