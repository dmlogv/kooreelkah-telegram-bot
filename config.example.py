"""
kooreelkah-telegram-bot uses simple py file for the configuration.

Be careful.

Very.
"""
from helpers import Answer, Member, Group

# Telegram Bot Token. Ask @BotFather if you have any questions.
TOKEN = '107886057:BAHQGP58QAJeyQzrWRM6HiSWfWVPDkJfBjE'

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
           Answer(r'\bNo\W*$', 'Got no.')]
