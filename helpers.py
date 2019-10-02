def split_chars(s, maxsplit=None):
    chars = list(s)

    if maxsplit:
        maxsplit = min(maxsplit, len(s) - 1)
        chars = chars[:maxsplit] + [''.join(chars[maxsplit:])]

    return chars


class Chat:
    """Telegram chat config item"""
    def __init__(self, chat_id):
        self.chat_id = chat_id


class Member(Chat):
    """Telegram chat member"""

    def as_link(self, text):
        """Get Telegram mention link

        Args:
            text: Link text"""
        return f'[{text}](tg://user?id={self.chat_id})'


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

    def mention_all(self):
        """Uses phrase to build TG mention link"""
        max_len = len(self.members)
        phrase_chars = split_chars(self.phrase, maxsplit=max_len - 1)
        links = [m.as_link(c) for m, c in zip(self.members, phrase_chars)]
        return ''.join(links)
