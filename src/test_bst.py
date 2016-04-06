# _*_ encoding: utf-8 _*_
"""Tests for binary search tree."""
from bst import Bst
import pytest


@pytest.fixture
def instance():
    tree = Bst()
    return tree


def test_new_tree(instance):
    """Test that our tree is a tree."""
    assert isinstance(instance, Bst)

