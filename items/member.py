from .chat import Chat


class Member(Chat):
    """Telegram chat member"""

    def as_link(self, text):
        """Get Telegram mention link

        Args:
            text: Link text"""
        return f'[{text}](tg://user?id={self.chat_id})'