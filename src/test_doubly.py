# _*_ encoding: utf-8 _*_
import pytest
"""Test linked_list.py."""

INSERT_ITEMS = [(['one', 'two', 'three', 'four'], 4)]
PREV_VAL = [(['one', 'two', 'three', 'four'], 'two')]
POP = [(['one', 'two', 'three', 'four'], None)]

def test_inheritance():
    from doubly_linked import DoublyLinked
    from linked_list import LinkedList
    new_list = DoublyLinked()
    assert isinstance(new_list, LinkedList)


@pytest.mark.parametrize('li, result', INSERT_ITEMS)
def test_insert(li, result):
    from doubly_linked import DoublyLinked
    new_list = DoublyLinked()
    new_list.insert(li)
    assert new_list.size() == 4


@pytest.mark.parametrize('li, result', PREV_VAL)
def test_prev(li, result):
    from doubly_linked import DoublyLinked
    new_list = DoublyLinked()
    new_list.insert(li)
    assert new_list.search('three').prev_node.get_data() == result


@pytest.mark.parametrize('li, result', PREV_VAL)
def test_prev_2(li, result):
    from doubly_linked import DoublyLinked
    new_list = DoublyLinked()
    for item in li[::-1]:
        new_list.insert(item)
    assert new_list.search('three').prev_node.get_data() == result


@pytest.mark.parametrize('li, result', POP)
def test_pop(li, result):
    from doubly_linked import DoublyLinked
    new_list = DoublyLinked()
    new_list.insert(li)
    assert new_list.pop().get_data() == 'one'
