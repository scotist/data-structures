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
    import random
    tree = Bst()
    for n in random.sample(range(1000), 20):
        tree.insert(n)


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
