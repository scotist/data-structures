# _*_ encoding: utf-8 _*_
"""Test stack.py."""

def test_stack():
    """Test list constructor."""
    from stack import Stack
    stacky = Stack()
    assert isinstance(stacky, Stack)

def test_push():
    from stack import Stack
    stacky = Stack()
    stacky.push(5)
    assert stacky.head.get_data() == 5

def test_pop():
    from stack import Stack
    stacky = Stack()
    stacky.push(1)
    assert stacky.pop().get_data() == 1
