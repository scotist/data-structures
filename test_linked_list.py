# _*_ encoding: utf-8 _*_
"""Test linked_list.py."""


def test_new_list():
    """Test list constructor."""
    from linked_list import LinkedList
    new_list = LinkedList()
    assert isinstance(new_list, LinkedList)
