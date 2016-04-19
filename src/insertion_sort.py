# _*_ encoding: utf-8 _*_
"""Implementation of Insertion Sort Algorithm."""
import timeit


def insertion_sort(seq):
    """Sort inserted values by insertion sort algorithm."""
    for index in range(1, len(seq)):
        value = seq[index]
        pos = index
        while pos > 0 and seq[pos - 1] > value:
            seq[pos], seq[pos - 1] = seq[pos - 1], seq[pos]
            pos -= 1
        seq[pos] = value
    return seq


if __name__ == "__main__":
    list_one = [x for x in range(0, 10000)]
    time1 = timeit.timeit("insertion_sort(list_one)", setup="from __main__ import insertion_sort, list_one", number=1000)
    print("""Best case scenario for insertion sort algorithm:
          list one is a list of all the integers from one to ten thousand in ascending order.""".format(time1))
    print("""Test runs: 1000
          Average Time = {}""".format(time1))

    list_two = [x for x in range(0, 10000)]
    list_two.reverse()
    time2 = timeit.timeit("insertion_sort(list_one)", setup="from __main__ import insertion_sort, list_one", number=1000)
    print("""In an example of the worst case scenario, list two is the reverse of list one: ten thousand to zero in descending order.""" )
    print("""Test runs: 1000
          Average Time = {}""".format(time2))
