# -*- coding:utf-8 -*-
"""Test priority queue."""
import pytest


def test_init():
    """Test init function."""
    from priority import Priority
    new_p_q = Priority()
    assert isinstance(new_p_q, Priority)


def test_insert():
    """Test insert function to empty queue."""
    from priority import Priority
    new_p_q = Priority()
    new_p_q.insert("monkey", 1)
    assert new_p_q.priority_queue[1] == ["monkey"]


def test_insert_01():
    """Test insert function to populated queue."""
    from priority import Priority
    new_p_q = Priority([("monkey", 1), ("dog", 1)])
    new_p_q.insert("cat", 2)
    assert new_p_q.priority_queue[2] == ["cat"]


def test_pop():
    """Test pop function on populated queue."""
    from priority import Priority
    new_p_q = Priority([("monkey", 1), ("cat", 2), ("dog", 1)])
    assert new_p_q.pop() == ("monkey")


def test_pop_fail():
    """Test pop function on empty queue."""
    from priority import Priority
    new_p_q = Priority()
    with pytest.raises(IndexError):
        new_p_q.pop()


def test_peek():
    """Test peek function on populated queue."""
    from priority import Priority
    new_p_q = Priority([("monkey", 1), ("cat", 2), ("dog", 1)])
    assert new_p_q.peek() == ("monkey")


def test_peek_fail():
    """Test peek function on empty queue."""
    from priority import Priority
    new_p_q = Priority()
    with pytest.raises(IndexError):
        new_p_q.peek()
