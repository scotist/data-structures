# _*_ encoding: utf-8 _*_
"""Test linked_list.py."""


def test_new_list():
    """Test list constructor."""
    from linked_list import LinkedList
    new_list = LinkedList()
    assert isinstance(new_list, LinkedList)


# def test_insert():
#     """Test insert method."""
#     from linked_list import LinkedList
#     new_list = LinkedList()
#     test_size = new_list.size()
#     new_list.insert("test")
#     assert test_size < new_list.size()

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
