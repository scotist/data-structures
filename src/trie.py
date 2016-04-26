# _*_ encoding: utf-8 _*_
"""Implement a trie structure in Python."""
import string


class Trie(object):
    """Make a trie structure."""

    def __init__(self):
        """Start the trie."""
        self._dict = {}

    def _input_check(self, token):
        """Check input type and value."""
        if not isinstance(token, str):
            raise TypeError('trie can only contain strings')
        if not token:
            raise ValueError('trie must contain a word')
        for letter in token:
            if letter not in string.ascii_letters + "'$-":
                raise ValueError('trie only contains real words')

    def insert(self, token):
        """Insert item into trie."""
        self._input_check(token)
        current_dict = self._dict
        for letter in token:
            current_dict = current_dict.setdefault(letter, {})
        current_dict['$'] = '$'

    def contains(self, token):
        """Check if word is contained in trie."""
        self._input_check(token)
        current_dict = self._dict
        try:
            for letter in token:
                current_dict = current_dict[letter]
            return current_dict['$'] == '$'
        except KeyError:
            return False


