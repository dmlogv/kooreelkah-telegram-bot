"""
kooreelkah-telegram-bot uses simple py file for the configuration.

Be careful.

Very.
"""
from datetime import time

from telegram.ext.jobqueue import Days

from items import AlternativeString, Answer, Member, Group, ScheduledMessage


# Telegram Bot Token. Ask @BotFather if you have any questions.
TOKEN = '107886057:BAHQGP58QAJeyQzrWRM6HiSWfWVPDkJfBjE'

# Id of the main chat (for boring daily routines)
CHAT = -349028917


# Explicitly create chat members for an interaction with them.
# Use charactonyms! (And see config.example.py)
RobertMartin = Member(7462)
DavidBowie = Member(9881233)
НиколайКолмогоров = Member(8429380)
GérardDepardieu = Member(2019234)
李舜臣 = Member(59123412)

MEMBERS = [RobertMartin, DavidBowie, НиколайКолмогоров, GérardDepardieu, 李舜臣]


# Create some group for your members
all = Group(['a', 'all'], 'Hey guys!', *MEMBERS)
actors = Group(['act', 'actors'], 'Hey actors,', DavidBowie, GérardDepardieu)

# Don't forget to add it to GROUPS list
GROUPS = [all, actors]


# Simple answers to react on user messages
ANSWERS = [Answer(r'[A-ZА-Я]{4,}', 'Don`t scream at us!', flags=0),
           Answer(r'\bNo\W*$', AlternativeString('Got no.', 'Have no.', 'Chuck No.'))]


# Scheduled messages
SCHEDULED = [ScheduledMessage(CHAT, 'Good morning!',
                              time(7, 0, 0), group=all),
             ScheduledMessage(CHAT, 'Happy friday!',
                              time(9, 0, 0), days=Days.FRI, group=all)]
