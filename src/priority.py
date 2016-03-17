# -*- coding: utf-8 -*-
"""Create a priority queue list."""


class Priority(object):
    """Defines a priority queue."""

    def __init__(self, values=[]):
        """Initalize the queue chain."""
        self.priority_queue = {}
        if isinstance(values, list):
            try:
                for value, priority in values:
                    self.insert(value, priority)
            except ValueError:
                raise TypeError("You need to tuplize your priorities")
        else:
            raise TypeError("Put your items in a list")

    def insert(self, value, priority=2):
        """Insert value into Priority Queue based on Priority."""
        if not isinstance(priority, int):
            raise TypeError("Priority must be an integer")
        if priority in self.priority_queue:
            self.priority_queue[priority].append(value)
        else:
            self.priority_queue[priority] = [value]
        print(self.priority_queue)

    def pop(self):
        """The the next item with the highest priority off the queue."""
        if len(self.priority_queue.values()):
            nextkey = 0
            while nextkey not in self.priority_queue:
                nextkey += 1
            up_next = self.priority_queue[nextkey][0]
            self.priority_queue[nextkey] = self.priority_queue[nextkey][1:]
            return up_next
        else:
            raise IndexError("There's nothing in your queue")

    def peek(self):
        """Return the upcoming highest priority item."""
        if len(self.priority_queue.values()):
            nextkey = 0
            while nextkey not in self.priority_queue:
                nextkey += 1
            return self.priority_queue[nextkey][0]
        else:
            raise IndexError("There's nothing in your queue")
