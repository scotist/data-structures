# _*_ encoding: utf-8 _*_
"""Implement radix sort algorithm in Python."""


def radix_sort(a_list, places=5):
    """Radix sort for positive numbers up a specified number of decimal places."""
    buckets = [[] for x in range(10)]
    for digit in range(places):
        for number in a_list:
            buckets[number // 10 ** digit % 10].append(number)
        del a_list[:]
        for bucket in buckets:
            a_list.extend(bucket)
            del bucket[:]
    return a_list


if __name__ == "__main__":
    from time_sorting import time_sorting
    time_sorting(radix_sort)
