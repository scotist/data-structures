# _*_ encoding: utf-8 _*_
import math

class Heap(object):
    """Make a binary heap."""

    def __init__(self, val=None):
        """Create heap."""
        self._container = Heap_Tools(val)


    def pop():
        """Pop first item off of heap."""

    def push(self, heap, val):
        """Push value into heap."""
        self.heap.append(val)
        if val < Heap[len(self.heap) - 1]:
            self._container.place_finder(val, len(self.heap - 1))



class Heap_Tools(object):
    """Orders list into a heap."""

    def __init__(self, val):
        """Initialize heap."""
        if isinstance(val, list):
            self.heap = val
        else:
            self.heap = []

    def place_finder(self, heap, index):
        """Puts value in correct position."""

    def parent(self, heap, i):
        if i == 0:
            return None
        return math.floor((i - 1) / 2)


