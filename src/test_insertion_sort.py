# _*_ encoding: utf-8 _*_
"""Test Implementation of Insertion Sort Algorithm."""

import random
import pytest

RANDOM_INSTANCES = [random.sample(range(1000),
                    random.randrange(2, 4)) for n in range(50)]


@pytest.mark.parametrize("seq", RANDOM_INSTANCES)
def test_insertion_sort(seq):
    """Test insertion sort results equal build-in python sort results."""
    from insertion_sort import insertion_sort
    assert insertion_sort(seq) == sorted(seq)


def test_sort_simple():
    """Test on simple case."""
    from insertion_sort import insertion_sort
    a_list = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert insertion_sort(a_list) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
