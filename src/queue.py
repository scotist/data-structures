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
