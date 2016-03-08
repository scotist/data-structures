from linked_list import LinkedList
# from linked_list import Node


class Stack(object):

    def __init__(self):
        self._container = LinkedList()

    def push(self, val):
        self._container.insert(val)
        self.head = self._container.head



    def pop(self):
        return self._container.pop()


