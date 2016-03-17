# _*_ encoding: utf-8 _*_
import math


class Heap(object):
    """Create Heap object with its methods."""
    def __init__(self, val=None):
        """Initialize Heap with or without initial values."""
        self.heap = []
        if val:
            for item in val:
                print(self.heap)
                self.push_heap(item)

    def push_heap(self, val):
        """Push value into the heap."""
        self.heap.append(val)
        self._heap_sort_toward_root(0, len(self.heap) - 1)

    def pop_heap(self):
        """Pop the top item off the heap."""
        if not len(self.heap):
            raise IndexError("Your heap is empty! You cannot pop.")
        self.heap[0] = self.heap[len(self.heap) - 1]
        self.heap.pop()
        print(self.heap)
        self._heap_sort_from_root(0)

    def _heap_sort_toward_root(self, limit_index, index):
        """Sort from small value at the end of the heap to the root."""
        new = self.heap[index]
        while index > limit_index:
            parentindex = (index - 1) >> 1
            parent = self.heap[parentindex]
            if new > parent:
                self.heap[index] = parent
                index = parentindex
                continue
            break
        self.heap[index] = new

    def _heap_sort_from_root(self, index):
        """Sort from the root to the appropriate spot on the heap."""
        end = len(self.heap)
        limit_index = index
        new = self.heap[index]
        childindex = (2 * index) + 1
        while childindex < end:
            right_index = childindex + 1
            if right_index < end and self.heap[right_index] > self.heap[childindex]:
                childindex = right_index
            self.heap[index] = self.heap[childindex]
            index = childindex
            childindex = (2 * index) + 1
        self.heap[index] = new
        self._heap_sort_toward_root(limit_index, index)
