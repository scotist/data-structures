# _*_ encoding: utf-8 _*_
import math


class Heap(object):

    def __init__(self, val=None):
        self.heap = []
        if val:
            for item in val:
                print(self.heap)
                self.push_heap(item)

    def push_heap(self, val):
        self.heap.append(val)
        self.heap_sort_toward_root(0, len(self.heap) - 1)

    def pop_heap(self):
        self.heap[0] = self.heap[len(self.heap) - 1]
        self.heap.pop()
        print(self.heap)
        self.heap_sort_from_root(0)

    def heap_sort_toward_root(self, limit_index, index):
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

    def heap_sort_from_root(self, index):
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
        self.heap_sort_toward_root(limit_index, index)


# class Heap(object):
#     """Make a binary heap."""

#     def __init__(self, val=None):
#         """Create heap."""
#         self._container = Heap_Tools(val)


#     def pop():
#         """Pop first item off of heap."""

#     def push(self, heap, val):
#         """Push value into heap."""
#         self.heap.append(val)
#         if val < Heap[len(self.heap) - 1]:
#             self._container.place_finder(val, len(self.heap - 1))



# class Heap_Tools(object):
#     """Orders list into a heap."""

#     def __init__(self, val):
#         """Initialize heap."""
#         if isinstance(val, list):
#             self.heap = val
#         else:
#             self.heap = []

#     def place_finder(self, heap, index):
#         """Puts value in correct position."""

#     def parent(self, heap, i):
#         if i == 0:
#             return None
#         return math.floor((i - 1) / 2)


