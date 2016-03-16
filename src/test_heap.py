# _*_ encoding: utf-8 _*_
"""Test heap.py."""

import math


def test_push_heap():
    from heap import Heap
    new_heap = Heap([16, 14, 10, 9, 8, 7, 3])
    new_heap.push_heap(100)
    assert new_heap.heap[0] == 100


def test_pop_heap():
    from heap import Heap
    second_heap = Heap([16, 14, 10, 9, 8, 7, 3])
    second_heap.pop_heap()
    # print(new_heap.heap)
    assert second_heap.heap == [14, 9, 10, 3, 8, 7]



# def test_heap_sort_toward_root:
#     from heap import heap_sort_toward_root


# def test_heap_sort_from_root:
#     from heap import heap_sort_from_root



# def test_inheritance():
#     """Test init from heap."""
#     from heap import Heap
#     from heap import Heap_Tools
#     new_heap = Heap()
#     assert isinstance(new_heap._container, Heap_Tools)



# # def test_heapify(A, i):
# #     assert(False)


# def test_root_parent():
#     from heap import Heap
#     new_heap = Heap(heap)
#     assert new_heap._container.parent(new_heap, 0) == None
#     print("pass")


# def test_a_parent():
#     assert(False)


# def test_a_left():
#     left(i)


# def test_a_right():
#     assert(False)


# def test_push():
#     n = 11
#     assert(False)


# def test_pop():
#     asset(False)


