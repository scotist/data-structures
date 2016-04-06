# _*_ encoding: utf-8 _*_
"""Tests for binary search tree."""
from bst import Bst
import pytest


@pytest.fixture
def empty_instance():
    tree = Bst()
    return tree


@pytest.fixture
def instance():
    tree = Bst()
    for n in range(20):
        tree.insert(n)
    return tree


def test_new_tree(instance):
    """Test that our tree is a tree."""
    assert isinstance(instance, Bst)


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


def test_contains(instance):
    """Test contains method."""
    for n in range(20):
        assert instance.contains(n)


def test_contains_2(instance):
    """Test false example for contains method."""
    assert not instance.contains(1000)


def test_size(instance):
    """Test size method."""
    assert instance.size() == 20


def test_size_1(empty_instance):
    """Test size method on empty tree."""
    assert empty_instance.size() == 0


def test_depth(instance):
    """Test depth method."""
    assert instance.depth() == 20


def test_depth_empty(empty_instance):
    """Test depth method on empty tree."""
    assert empty_instance.depth() == 0
