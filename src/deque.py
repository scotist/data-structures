# _*_ encoding: utf-8 _*_
from queue import Queue


class Deque(object):
    """Make deque object."""
    def __init__(self, val=None):
        self._container_q = Queue(val)

    def pop(self):
        return self._container_q._container.shift()

    def pop_left(self):
        return self._container_q._container.pop()

    def append(self, val):
        self._container_q._container.append(val)

    def append_left(self, val):
        self._container_q._container.insert(val)

    def peek(self):
        cur = self._container_q._container.head
        if cur == self._container_q._container._mark:
            return None
        while cur.next_node != self._container_q._container._mark:
            cur = cur.next_node
        return cur.get_data()

    def peek_left(self):
        cur = self._container_q._container.head
        if cur == self._container_q._container._mark:
            return None
        return self._container_q.peek()

    def size(self):
        return self._container_q.size()
