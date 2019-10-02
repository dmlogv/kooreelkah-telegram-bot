class Chat:
    """Telegram chat config item"""
    def __init__(self, chat_id):
        self.chat_id = chat_id


class Member(Chat):
    """Telegram chat member"""


class Group:
    """Union Members to group

    Args:
        commands (str, list[str]): Telegram bot commands to mention group members
        phrase: Phrase will be used to mention members.
            len(phrase) must be equal or grater than len(members)
        members (list[Member]): members of group
    """
    def __init__(self, commands, phrase, *members):
        if not (type(commands) in (str, list)):
            raise ValueError('Group command must be str or list')
        if not all(isinstance(m, Member) for m in members):
            raise ValueError('Group members must be instances of Member')
        if len(phrase) < len(members):
            raise ValueError('Length of member phrase must be >= length of members list')

        self.commands = commands
        self.phrase = phrase
        self.members = members