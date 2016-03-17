# _*_ encoding: utf-8 _*_
"""Test heap.py."""
import pytest
import math


def test_new_heap():
    """Test heap instance is an instance of the heap class."""
    from heap import Heap
    a_heap = Heap()
    assert isinstance(a_heap, Heap)


def test_sort_heap_toward_root():
    """Test heaps can be sorted toward the root."""
    from heap import Heap
    my_heap = Heap([14, 10, 16, 9, 8, 7, 3])
    my_heap._heap_sort_toward_root(0, 2)
    assert my_heap.heap == [16, 10, 14, 9, 8, 7, 3]


def test_sort_from_root():
    """Test heaps can be sorted away from the root."""
    from heap import Heap
    my_heap = Heap([16, 14, 10, 1, 9, 8, 7, 3])
    my_heap._heap_sort_from_root(3)
    assert my_heap.heap == [16, 14, 10, 3, 9, 8, 7, 1]


def test_push_heap():
    """Test the push heap method with a list given at instantiation."""
    from heap import Heap
    new_heap = Heap([16, 14, 10, 9, 8, 7, 3])
    new_heap.push_heap(100)
    assert new_heap.heap[0] == 100


def test_push_heap_01():
    """Test pushing an item into an empty heap."""
    from heap import Heap
    new_heap1 = Heap()
    new_heap1.push_heap(5)
    assert new_heap1.heap[0] == 5


def test_pop_heap():
    """Test popping an item out of a populated heap."""
    from heap import Heap
    second_heap = Heap([16, 14, 10, 9, 8, 7, 3])
    second_heap.pop_heap()
    assert second_heap.heap == [14, 9, 10, 3, 8, 7]


def test_pop_empty_heap():
    """Test appropriate error is raised when popping an empty heap."""
    from heap import Heap
    new_heap = Heap()
    with pytest.raises(IndexError):
        new_heap.pop_heap()
