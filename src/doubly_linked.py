from linked_list import LinkedList
from linked_list import Node

_mark = object()


class DoublyLinked(LinkedList):
    def insert(self, val):
        """Insert value at head of list."""
        if type(val) == list:
            for item in val[::-1]:
                new_node = DoubleNode(item, self.head)
                try:
                    self.head.set_previous(new_node)
                except AttributeError:
                    pass
                self.head = new_node
        else:
            new_node = DoubleNode(val, self.head)
            try:
                self.head.set_previous(new_node)
            except AttributeError:
                pass
            self.head = new_node

    def pop(self):
        """Pop the first value off the head of the list and return it."""
        item = self.head
        if item is _mark:
            raise IndexError
        else:
            self.head = item.get_next()
            self.head.set_previous = None
            return item


class DoubleNode(Node):
    """Double Node constructor for doubly linked list."""

    def __init__(self, data=None, next_node=None, prev_node=None):
        """Initialize the double node."""
        self.data = data
        self.prev_node = prev_node
        self.next_node = next_node

    def set_previous(self, prev):
        self.prev_node = prev
