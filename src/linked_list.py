# _*_ encoding: utf-8 _*_
"""Demonstrate linked list in python."""


class LinkedList(object):
    """Demonstrate linked list."""

    def __init__(self, head=None):
        """Initialize the list."""
        self.head = head

    def insert(self, val):
        """Insert value at head of list."""
        if type(val) == list:
            for item in val[::-1]:
                new_node = Node(item, self.head)
                self.head = new_node
        else:
            new_node = Node(val, self.head)
            self.head = new_node

    def pop(self):
        """Pop the first value off the head of the list and return it."""
        item = self.head
        if item is None:
            raise IndexError
        else:
            self.head = item.get_next()
            return item

    def size(self):
        """Return the length of the list."""
        counter = 0
        current_node = self.head
        while current_node is not None:
            counter += 1
            current_node = current_node.get_next()
        return counter

    def search(self, val):
        """Return the node containing 'val' in list if exists, else None."""
        current_node = self.head
        while current_node.get_data() is not val:
            current_node = current_node.get_next()
            if current_node is None:
                print("It's not there!")
                break
        return current_node
        print("Found it!")

    def remove(self, val):
        """Remove given node from list."""
        previous_node = None
        current_node = self.head
        while current_node.get_data() is not val.get_data():
            previous_node = current_node
            current_node = current_node.get_next()
            if current_node.get_data() is None:
                break
        if current_node.get_data() == val.get_data():
            previous_node.set_next(current_node.get_next())
        else:
            print('Not Found')

    def display(self):
        """Print list represented as Python tuple literal."""
        output = """"""
        current_node = self.head
        while current_node is not None:
            output += '{}, '.format(current_node.get_data())
            current_node = current_node.get_next()
        printable = '(' + output[:-2] + ')'
        print(printable)
        return printable


class Node(object):
    """Node constructor for linked list."""

    def __init__(self, data=None, next_node=None):
        """Initialize the node."""
        self.data = data
        self.next_node = next_node

    def get_data(self):
        """Get data for node."""
        return self.data

    def get_next(self):
        """Retrieve next node in list."""
        return self.next_node

    def set_next(self, next_node):
        """Set next node in list."""
        self.next_node = next_node

