# _*_ encoding: utf-8 _*_
"""Demonstrate doubly-linked list in python."""
from linked_list import Node


class DoublyLinked(object):
    """Implement a doubly-linked list from a singly-linked list."""

    def __init__(self, val=None):
        """Initialize the list."""
        self.head = object()
        self._mark = self.head
        if val:
            self.insert(val)

    def insert(self, val):
        """Insert value at head of list."""
        if isinstance(val, list):
            for item in val[::-1]:
                new_node = DoubleNode(item, self.head, self._mark)
                try:
                    self.head.set_previous(new_node)
                except AttributeError:
                    pass
                self.head = new_node
        else:
            new_node = DoubleNode(val, self.head, self._mark)
            try:
                self.head.set_previous(new_node)
            except AttributeError:
                pass
            self.head = new_node

    def pop(self):
        """Pop the first value off the head of the list and return it."""
        item = self.head
        if item is self._mark:
            raise IndexError
        else:
            self.head = item.get_next()
            try:
                self.head.set_previous(self._mark)
            except AttributeError:
                pass
            return item.get_data()

    def append(self, val):
        """Append the given item to the tail of the list."""
        cur = self.head
        if cur == self._mark:
            new_node = DoubleNode(val, self._mark)
            self.head = new_node
        else:
            new_node = DoubleNode(val, self._mark)
            while cur.next_node != self._mark:
                cur = cur.next_node
            cur.set_next(new_node)
            new_node.set_previous(cur)

    def shift(self):
        """Remove and returns the last value from the tail of the list."""
        cur = self.head
        if cur == self._mark:
            raise IndexError
        else:
            while cur.next_node != self._mark:
                cur = cur.next_node
            try:
                cur.prev_node.next_node = self._mark
            except AttributeError:
                raise IndexError
            return cur.get_data()

    def remove(self, value):
        """Remove the first occurrence of value in the list."""
        previous_node = None
        current_node = self.head
        while current_node.get_data() is not value:
            previous_node = current_node
            current_node = current_node.get_next()
            if current_node.get_data() is None:
                break
        if current_node.get_data() == value:
            previous_node.set_next(current_node.get_next())
        else:
            print('Not Found')


class DoubleNode(Node):
    """Double Node constructor for doubly linked list."""

    def __init__(self, data=None, next_node=None, prev_node=None):
        """Initialize the double node."""
        self.data = data
        self.prev_node = prev_node
        self.next_node = next_node

    def set_previous(self, prev):
        """Set previous node."""
        self.prev_node = prev
