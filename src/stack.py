# _*_ encoding: utf-8 _*_
"""Implement stack using linked list."""
from linked_list import LinkedList


class Stack(object):
    """Make stack object from linked list object."""

    def __init__(self):
        """Initialize stack."""
        self._container = LinkedList()

    def push(self, val):
        """Push item to stack."""
        self._container.insert(val)
        self.head = self._container.head

    def pop(self):
        """Pop item from stack."""
        return self._container.pop()
