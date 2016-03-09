from linked_list import LinkedList
from linked_list import Node


class DoublyLinked(LinkedList):

    def insert(self, val):
        """Insert value at head of list."""
        if type(val) == list:
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
            self.head.set_previous(self._mark)
            return item

    def append(self, val):
        """Append the given item to the tail of the list."""
        cur = self.head
        new_node = DoubleNode(val, self._mark)
        while cur.next_node != self._mark:
            cur = cur.next_node
        cur.set_next(new_node)
        new_node.set_previous(cur)

    def shift(self):
        """Removes and returns the last value from the tail of the list."""
        cur = self.head
        if cur == self._mark:
            raise IndexError
        else:
            while cur.next_node != self._mark:
                cur = cur.next_node
            cur.prev_node.next_node = self._mark
            return cur

    def remove(self, val):
        """Remove given node from list."""
        target = self.search(val)
        target.prev_node.next_node = target.next_node
        target.next_node.prev_node = target.prev_node
class DoubleNode(Node):
    """Double Node constructor for doubly linked list."""

    def __init__(self, data=None, next_node=None, prev_node=None):
        """Initialize the double node."""
        self.data = data
        self.prev_node = prev_node
        self.next_node = next_node

    def set_previous(self, prev):
        self.prev_node = prev
