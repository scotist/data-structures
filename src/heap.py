# _*_ encoding: utf-8 _*_
import math

# heap = []


def push_heap(heap, val):
    heap.append(val)
    heap_sort_toward_root(heap, 0, len(heap) - 1)


def pop_heap(heap):
    heap[0] = heap[len(heap) - 1]
    heap.pop()
    heap_sort_from_root(heap, 0)


def heap_sort_toward_root(heap, limit_index, index):
    new = heap[index]
    while index > limit_index:
        parentindex = (index - 1) >> 1
        parent = heap[parentindex]
        if new > parent:
            heap[index] = parent
            index = parentindex
            continue
        break
    heap[index] = new


def heap_sort_from_root(heap, index):
    end = len(heap)
    limit_index = index
    new = heap[index]
    childindex = (2 * index) + 1
    while childindex < end:
        right_index = childindex + 1
        if right_index < end and heap[right_index] > heap[childindex]:
            childindex = right_index
        heap[index] = heap[childindex]
        index = childindex
        childindex = (2 * index) + 1
    heap[index] = new
    heap_sort_toward_root(heap, limit_index, index)


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


