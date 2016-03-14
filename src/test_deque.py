# _*_ encoding: utf-8 _*_
import pytest

APPEND = [([1, 2, 3, 4], 'addme', 'addme'),
          (['Hey', 'there', 'Howdy'], 'addthis', 'addthis')]

POP_PEEK = [([3, 6, 2, 7, 7, 9], 9),
            ([4, 6, 2, 3], 3),
            ([], None)]

POPLEFT_PEEK = [([4, 6, 2, 3], 4),
                ([3, 6, 2, 7, 7, 9], 3),
                ([], None)]

SIZE = [([2, 3, 6, 7, 9, 9], 6),
        ([4, 3], 2),
        ([], 0)]


def test_composition_q():
    from deque import Deque
    from queue import Queue
    new_list = Deque()
    assert isinstance(new_list._container_q, Queue)


@pytest.mark.parametrize('li, result', POP_PEEK)
def test_pop(li, result):
    from deque import Deque
    new_list = Deque(li)
    if not li:
        with pytest.raises(IndexError):
            new_list.pop()
    else:
        assert new_list.pop() == result


@pytest.mark.parametrize('li, result', POPLEFT_PEEK)
def test_pop_left(li, result):
    from deque import Deque
    new_list = Deque(li)
    if not li:
        with pytest.raises(IndexError):
            new_list.pop_left()
    else:
        assert new_list.pop_left() == result


@pytest.mark.parametrize('li, result', POP_PEEK)
def test_peek(li, result):
    from deque import Deque
    new_list = Deque(li)
    assert new_list.peek() == result


@pytest.mark.parametrize('li, result', POPLEFT_PEEK)
def test_peek_left(li, result):
    from deque import Deque
    new_list = Deque(li)
    assert new_list.peek_left() == result


@pytest.mark.parametrize('li, added_item, result', APPEND)
def test_append(li, added_item, result):
    from deque import Deque
    new_list = Deque(li)
    new_list.append(added_item)
    assert new_list.pop() == result


def test_append_empty():
    from deque import Deque
    new_list = Deque()
    with pytest.raises(IndexError):
        new_list.pop()


@pytest.mark.parametrize('li, added_item, result', APPEND)
def test_append_left(li, added_item, result):
    from deque import Deque
    new_list = Deque(li)
    new_list.append_left(added_item)
    assert new_list.pop_left() == result


@pytest.mark.parametrize('li, result', SIZE)
def test_size(li, result):
    from deque import Deque
    new_list = Deque(li)
    assert new_list.size() == result
