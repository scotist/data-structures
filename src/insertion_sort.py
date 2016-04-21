# _*_ encoding: utf-8 _*_
"""Implementation of Insertion Sort Algorithm."""


def insertion_sort(seq):
    """Sort inserted values in place by insertion sort algorithm."""
    for index in range(1, len(seq)):
        value = seq[index]
        pos = index
        while pos > 0 and seq[pos - 1] > value:
            seq[pos], seq[pos - 1] = seq[pos - 1], seq[pos]
            pos -= 1
        seq[pos] = value


if __name__ == "__main__":
    from time_sorting import time_sorting
    time_sorting(insertion_sort)
