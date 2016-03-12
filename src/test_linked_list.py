# _*_ encoding: utf-8 _*_
"""Test linked_list.py."""


def test_new_list():
    """Test list constructor."""
    from linked_list import LinkedList
    new_list = LinkedList()
    assert isinstance(new_list, LinkedList)


def test_new_populated_list_0():
    """Test ability to make new list with value."""
    from linked_list import LinkedList
    new_list = LinkedList(1)
    assert new_list.size() == 1


def test_new_populated_list_1():
    """Test ability to make new list with value."""
    from linked_list import LinkedList
    new_list = LinkedList([1, 2])
    assert new_list.size() == 2


def test_insert():
    """Test insert method."""
    from linked_list import LinkedList
    new_list = LinkedList()
    test_size = new_list.size()
    new_list.insert("test")
    assert test_size < new_list.size()


def test_insert_list():
    """Test insert method with a list."""
    from linked_list import LinkedList
    new_list = LinkedList()
    new_list.insert([1, 2, 3])
    assert new_list.size() == 3


def test_size():
    """Test size method."""
    from linked_list import LinkedList
    new_list = LinkedList()
    new_list.insert("test")
    new_list.insert("kickass test")
    new_list.insert("negasonic ultra test")
    size = new_list.size()
    assert size == 3


def test_pop():
    """Test pop method."""
    from linked_list import LinkedList
    first_list = LinkedList()
    first_list.insert([1, 2, 3, 4])
    old_size = first_list.size()
    popped = first_list.pop()
    new_size = first_list.size()
    assert new_size < old_size
    assert popped == 1


def test_search():
    """Test search method."""
    from linked_list import LinkedList
    new_list = LinkedList()
    new_list.insert([1, 2, 3, 4])
    query = new_list.search(3)
    assert query.get_data() == 3


def test_remove():
    """Test remove method."""
    from linked_list import LinkedList
    new_list = LinkedList()
    new_list.insert([1, 2, 3, 4])
    new_list.remove(new_list.search(3))
    assert new_list.display() == '(1, 2, 4)'


def test_display():
    """Test display method."""
    from linked_list import LinkedList
    new_list = LinkedList()
    new_list.insert([1, 2, 3, 4])
    new_list.display()
    assert new_list.display() == '(1, 2, 3, 4)'


def test_node_creation():
    """Test new node."""
    from linked_list import Node
    new_node = Node("word")
    assert isinstance(new_node, Node)
    assert new_node.data == "word"


def test_get_data():
    """Test get_data method."""
    from linked_list import Node
    new_node = Node("word")
    assert new_node.get_data() == "word"


def test_get_next():
    """Test get_next method."""
    from linked_list import Node
    new_node = Node("word", "next")
    assert new_node.get_next() == "next"


def test_set_next():
    """Test get_next method."""
    from linked_list import Node
    new_node = Node("word", "chimichanga")
    new_node.set_next("next")
    assert new_node.get_next() == "next"
