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

