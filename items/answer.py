import re


class Answer:
    """Simple answer on user messages, matching with a regular expression"""
    def __init__(self, regex, text, flags=re.IGNORECASE):
        self.regex = re.compile(regex, flags=flags)
        self.text = text