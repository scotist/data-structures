# _*_ encoding: utf-8 _*_
import pytest
"""Test queue.py."""

SIZE = [(['one', 'two', 'three', 'four'], 4)]
DEQUEUE = [(['one', 'two', 'three', 'four'], 'one')]
ENQUEUE = [(['one'], 'one'),
           (['one', 'two', 'three'], 'three')]


def test_inheritance():
    """Test init from queue."""
    from doubly_linked import DoublyLinked
    from queue import Queue
    new_list = Queue()
    assert isinstance(new_list._container, DoublyLinked)


@pytest.mark.parametrize('li, result', ENQUEUE)
def test_enqueue_and_peek(li, result):
    """Test enqueue method."""
    from queue import Queue
    new_list = Queue()
    for item in li[::-1]:
        new_list.enqueue(item)
    assert new_list.peek() == result


@pytest.mark.parametrize('li, result', DEQUEUE)
def test_dequeue(li, result):
    """Test dequeue method."""
    from queue import Queue
    new_list = Queue()
    for item in li:
        new_list.enqueue(item)
    assert new_list.dequeue() == result
