# _*_ encoding: utf-8 _*_
"""Implement radix sort algorithm in Python."""
import timeit


def radix_sort(a_list):
    """Radix sort for positive numbers up to one hundred thousand."""
    buckets = [[] for x in range(10)]
    for digit in range(0, 5):
        for number in a_list:
            buckets[number // 10 ** digit % 10].append(number)
        del a_list[:]
        for bucket in buckets:
            a_list.extend(bucket)
            del bucket[:]
    return a_list


if __name__ == "__main__":
    list_one = list(range(990))
    tries = 10000
    time1 = timeit.timeit("radix_sort(list_one)", setup="from __main__ import radix_sort, list_one", number=tries)
    print("""Best case scenario for merge sort algorithm:
          list one is a list of all the integers from one to ten thousand in ascending order.""".format(time1))
    print("""Test runs: 10000
          Average Time = {}""".format(time1 / tries))

    list_two = list(range(990))
    list_two.reverse()
    time2 = timeit.timeit("radix_sort(list_one)", setup="from __main__ import radix_sort, list_one", number=tries)
    print("""In an example of the worst case scenario, list two is the reverse of list one: ten thousand to zero in descending order.""" )
    print("""Test runs: 10000
          Average Time = {}""".format(time2 / tries))
