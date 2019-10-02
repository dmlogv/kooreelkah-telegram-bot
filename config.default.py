"""
kooreelkah-telegram-bot uses simple py file for the configuration.

Be careful.

Very.
"""
from helpers import Answer, Member, Group

# Telegram Bot Token. Ask @BotFather if you have any questions.
TOKEN = ''

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
ANSWERS = [Answer()]
