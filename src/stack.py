# _*_ encoding: utf-8 _*_
"""Implement stack using linked list."""
from linked_list import LinkedList


class Stack(object):

    def __init__(self):
        self._container = LinkedList()


    def push(self, val):
        self._container.insert(val)
        self.head = self._container.head


    def pop(self):
        return self._container.pop()


