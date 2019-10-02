import unittest

from helpers import split_chars, Member, Group


class SplitCharsTest(unittest.TestCase):
    def test_just_split(self):
        self.assertListEqual(['H', 'i', ',', ' ', 'a', 'l', 'l', '!'],
                             split_chars('Hi, all!'))

    def test_split_maxsplit(self):
        self.assertListEqual(['H', 'i, all!'],
                             split_chars('Hi, all!', maxsplit=1))
        self.assertListEqual(['H', 'i', ', all!'],
                             split_chars('Hi, all!', maxsplit=2))

    def test_split_corner_maxsplits(self):
        self.assertListEqual(['H', 'i', ',', ' ', 'a', 'l', 'l', '!'],
                             split_chars('Hi, all!', maxsplit=-1))
        self.assertListEqual(['H', 'i', ',', ' ', 'a', 'l', 'l', '!'],
                             split_chars('Hi, all!', maxsplit=0))
        self.assertListEqual(['H', 'i', ',', ' ', 'a', 'l', 'l', '!'],
                             split_chars('Hi, all!', maxsplit=100))


class MemberTest(unittest.TestCase):
    def setUp(self):
        self.mike = Member(1234)

    def test_as_link(self):
        self.assertEqual('[Mike](tg://user?id=1234)', self.mike.as_link('Mike'))


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


class GroupMentionTest(unittest.TestCase):
    def setUp(self):
        self.members = [Member(123), Member(456), Member(789)]

    def test_equal_phrase(self):
        expected = ('[H](tg://user?id=123)'
                    '[i](tg://user?id=456)'
                    '[,](tg://user?id=789)')
        self.assertEqual(expected, Group('a', 'Hi,', *self.members).mention_all())

    def test_greater_phrase(self):
        expected = ('[H](tg://user?id=123)'
                    '[i](tg://user?id=456)'
                    '[, all](tg://user?id=789)')
        self.assertEqual(expected, Group('a', 'Hi, all', *self.members).mention_all())
