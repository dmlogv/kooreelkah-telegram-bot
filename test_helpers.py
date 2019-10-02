import unittest

from helpers import Member, Group


class GroupInitTest(unittest.TestCase):
    def setUp(self):
        self.members = [Member(123), Member(456), Member(789)]

    def test_valid_groups(self):
        self.assertListEqual(self.members,
                             list(Group('mem', 'Phrase,', *self.members).members))

    def test_command(self):
        with self.assertRaises(ValueError):
            Group(123, 'Phrase', *self.members)
        Group('soup', 'Phrase', *self.members)
        Group(['soup', 'borsch'], 'Phrase', *self.members)

    def test_short_phrase(self):
        with self.assertRaises(ValueError):
            Group('a', 'b', *self.members)

    def test_invalid_members(self):
        with self.assertRaises(ValueError):
            Group('m', 'phrase', self.members)
        with self.assertRaises(ValueError):
            Group('m', 'phrase', None)
        with self.assertRaises(ValueError):
            Group('m', 'phrase', Member(123), 1, Member(456))
