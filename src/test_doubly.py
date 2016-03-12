# _*_ encoding: utf-8 _*_
"""Test linked_list.py."""
import pytest

INSERT_ITEMS = [(['one', 'two', 'three', 'four'], 4)]
PREV_VAL = [(['one', 'two', 'three', 'four'], 'two')]
POP = [(['one', 'two', 'three', 'four'])]
APPEND = [(['one', 'two', 'three'], 'three')]
SHIFT = [(['one', 'two', 'three', 'four'], 'four'),
         (['five', 'hat', 'bunny', 'dude'], 'dude')]
EMPTY = [([])]
REMOVE = [(['one', 'two', 'three', 'four', 'five'], 'three', 'two', 'four', 4),
          (['Hello', 'This', 'is', 'a', 'test'], 'a', 'is', 'test', 4)]


def test_new_list():
    """Test list constructor."""
    from doubly_linked import DoublyLinked
    new_list = DoublyLinked()
    assert isinstance(new_list, DoublyLinked)


# @pytest.mark.parametrize('li, result', INSERT_ITEMS)
# def test_insert(li, result):
#     from doubly_linked import DoublyLinked
#     new_list = DoublyLinked()
#     new_list.insert(li)
#     assert new_list.size() == 4


# @pytest.mark.parametrize('li, result', PREV_VAL)
# def test_prev(li, result):
#     from doubly_linked import DoublyLinked
#     new_list = DoublyLinked()
#     new_list.insert(li)
#     assert new_list.search('three').prev_node.get_data() == result


# @pytest.mark.parametrize('li, result', PREV_VAL)
# def test_prev_2(li, result):
#     from doubly_linked import DoublyLinked
#     new_list = DoublyLinked()
#     for item in li[::-1]:
#         new_list.insert(item)
#     assert new_list.search('three').prev_node.get_data() == result


@pytest.mark.parametrize('li', POP)
def test_pop(li):
    """Test pop function."""
    from doubly_linked import DoublyLinked
    new_list = DoublyLinked()
    new_list.insert(li)
    assert new_list.pop() == 'one'
    try:
        new_list.head.prev_node
    except AttributeError:
        assert True


# @pytest.mark.parametrize('li, result', APPEND)
# def test_append(li, result):
#     from doubly_linked import DoublyLinked
#     new_list = DoublyLinked()
#     new_list.insert(li)
#     new_list.append('four')
#     print(result)
#     assert new_list.search('four').prev_node.get_data() == result
#     assert new_list.search('four').get_next() == new_list._mark


@pytest.mark.parametrize('li, result', SHIFT)
def test_shift(li, result):
    from doubly_linked import DoublyLinked
    new_list = DoublyLinked()
    new_list.insert(li)
    assert new_list.shift().get_data() == result


@pytest.mark.parametrize('li', EMPTY)
def test_shift_empty(li):
    from doubly_linked import DoublyLinked
    new_list = DoublyLinked()
    new_list.insert(li)
    with pytest.raises(IndexError):
        new_list.shift()


# @pytest.mark.parametrize('li, remove_me, prev, next_item, size', REMOVE)
# def test_remove(li, remove_me, prev, next_item, size):
#     from doubly_linked import DoublyLinked
#     new_list = DoublyLinked()
#     new_list.insert(li)
#     new_list.remove(remove_me)
#     assert new_list.size() == size
#     assert new_list.search(prev).next_node == new_list.search(next_item)
#     assert new_list.search(next_item).prev_node == new_list.search(prev)
