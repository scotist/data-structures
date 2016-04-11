# _*_ encoding: utf-8 _*_
"""Tests for binary search tree."""
from bst import Bst
import pytest


@pytest.fixture
def empty_instance():
    """Empty tree fixture."""
    tree = Bst()
    return tree


@pytest.fixture
def instance():
    """Full tree fixture."""
    tree = Bst()
    for n in range(20):
        tree.insert(n)
    return tree


@pytest.fixture
def instance2():
    """Fun tree fixture."""
    fun_tree = Bst()
    insertions = [7, 6, 10, 5, 20, 11]
    for fun in insertions:
        fun_tree.insert(fun)
    return fun_tree


def test_new_tree(instance):
    """Test that our tree is a tree."""
    assert isinstance(instance, Bst)


def test_new_empty_tree(empty_instance):
    """Test that an empty tree is still a tree."""
    assert all([
        empty_instance.value is None,
        empty_instance.parent is None,
        empty_instance.left_child is None,
        empty_instance.right_child is None])


def test_insert(empty_instance):
    """Test insert method on empty tree."""
    empty_instance.insert(0)
    assert empty_instance.contains(0)


def test_insert_many(empty_instance):
    """Test insert method with many values."""
    insertions = list(range(12))
    for chump in insertions:
        empty_instance.insert(chump)
    for chump in insertions:
        assert empty_instance.contains(chump)


def test_insert_fail(instance):
    """Test insert method with badly mixed values."""
    with pytest.raises(TypeError):
        instance.insert("This can't go here!")


def test_insert_fail_2(instance):
    """Test insert method with None value."""
    with pytest.raises(TypeError):
        instance.insert(None)


def test_contains(instance):
    """Test contains method."""
    for n in range(20):
        assert instance.contains(n)


def test_contains_false(instance):
    """Test false example for contains method."""
    assert not instance.contains(1000)


def test_size(instance):
    """Test size method."""
    assert instance.size() == 20


def test_size_empty(empty_instance):
    """Test size method on empty tree."""
    assert empty_instance.size() == 0


def test_depth(instance):
    """Test depth method."""
    assert instance.depth() == 20


def test_depth_empty(empty_instance):
    """Test depth method on empty tree."""
    assert empty_instance.depth() == 0


def test_depth_fun(instance2):
    """Test depth method on more complex tree."""
    assert instance2.depth() == 4


def test_balance(instance2):
    """Test balance method on right-unbalanced tree."""
    assert instance2.balance() == -1


def test_balance_balanced(instance2):
    """Test balance method on balanced tree."""
    instance2.insert(3)
    assert instance2.balance() == 0


def test_balance_left(instance2):
    """Test balance method on left-unbalanced tree."""
    instance2.insert(3)
    instance2.insert(2)
    assert instance2.balance() == 1


def test_balance_extreme_right(instance):
    """Test balance method on extremely-unbalanced tree."""
    assert instance.balance() == - 19
