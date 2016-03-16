# _*_ encoding: utf-8 _*_
"""Test linked_list.py."""
import pytest

INSERT_ITEMS = [(['one', 'two', 'three', 'four'], 'one')]
POP = [(['one', 'two', 'three', 'four'])]
APPEND = [(['one', 'two', 'three'], 'four')]
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


@pytest.mark.parametrize('li, result', INSERT_ITEMS)
def test_insert(li, result):
    """Test insert function."""
    from doubly_linked import DoublyLinked
    new_list = DoublyLinked()
    new_list.insert(li)
    new_list.pop()
    assert result == 'one'


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


@pytest.mark.parametrize('li, result', APPEND)
def test_append(li, result):
    from doubly_linked import DoublyLinked
    new_list = DoublyLinked()
    new_list.insert(li)
    new_list.append('four')
    assert result == new_list.shift()


@pytest.mark.parametrize('li, result', SHIFT)
def test_shift(li, result):
    from doubly_linked import DoublyLinked
    new_list = DoublyLinked()
    new_list.insert(li)
    assert new_list.shift() == result


@pytest.mark.parametrize('li', EMPTY)
def test_shift_empty(li):
    from doubly_linked import DoublyLinked
    new_list = DoublyLinked()
    new_list.insert(li)
    with pytest.raises(IndexError):
        new_list.shift()


def test_remove():
    from doubly_linked import DoublyLinked
    new_list = DoublyLinked()
    new_list.insert([1, 2, 3])
    new_list.remove(3)
    assert new_list.shift() == 2
