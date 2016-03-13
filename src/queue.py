# _*_ encoding: utf-8 _*_
"""Demonstrate queue in python using a doubly-linked list."""

from doubly_linked import DoublyLinked


class Queue(object):
    """Make queue object from doubly-linked list object."""

    def __init__(self):
        """Initialize queue."""
        self._container = DoublyLinked()

    def enqueue(self, val):
        """Push item to queue."""
        self._container.append(val)

    def dequeue(self):
        """Remove item from head queue and return its value."""
        return self._container.pop()

    def peek(self):
        """Return next value in queue."""
        if self._container.head is self._container._mark:
            return None
        else:
            return self._container.head.get_data()

    def size(self):
        """Return the length of the list."""
        counter = 0
        current_node = self._container.head
        while current_node is not self._container._mark:
            counter += 1
            current_node = current_node.get_next()
        return counter
