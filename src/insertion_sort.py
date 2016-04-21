# _*_ encoding: utf-8 _*_
"""Implementation of Insertion Sort Algorithm."""
import timeit


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
    list_one = list(range(990))
    tries = 10000
    time1 = timeit.timeit("insertion_sort(list_one)", setup="from __main__ import insertion_sort, list_one", number=tries)
    print("""Best case scenario for insertion sort algorithm:
          list one is a list of all the integers from one to ten thousand in ascending order.""".format(time1))
    print("""Test runs: 10000
          Average Time = {}""".format(time1 / tries))

    list_two = list(range(990))
    list_two.reverse()
    time2 = timeit.timeit("insertion_sort(list_one)", setup="from __main__ import insertion_sort, list_one", number=tries)
    print("""In an example of the worst case scenario, list two is the reverse of list one: ten thousand to zero in descending order.""" )
    print("""Test runs: 10000
          Average Time = {}""".format(time2 / tries))
