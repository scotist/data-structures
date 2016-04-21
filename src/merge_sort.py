"""Implement merge sort algorithm."""
import timeit


def merge_sort(seq):
    """Merge Sort Function."""
    length = len(seq)
    if length < 2:
        return
    middle = length // 2
    left = seq[:middle]
    right = seq[middle:]
    merge_sort(left)
    merge_sort(right)
    i_left = 0
    i_right = 0
    i_seq = 0
    while i_left < len(left) and i_right < len(right):
        if left[i_left] < right[i_right]:
            seq[i_seq] = left[i_left]
            i_left += 1
        else:
            seq[i_seq] = right[i_right]
            i_right += 1
        i_seq += 1

    while i_left < len(left):
        seq[i_seq] = left[i_left]
        i_left += 1
        i_seq += 1

    while i_right < len(right):
        seq[i_seq] = right[i_right]
        i_right += 1
        i_seq += 1

if __name__ == "__main__":
    list_one = list(range(990))
    tries = 10000
    time1 = timeit.timeit("merge_sort(list_one)", setup="from __main__ import merge_sort, list_one", number=tries)
    print("""Best case scenario for merge sort algorithm:
          list one is a list of all the integers from one to ten thousand in ascending order.""".format(time1))
    print("""Test runs: 10000
          Average Time = {}""".format(time1 / tries))

    list_two = list(range(990))
    list_two.reverse()
    time2 = timeit.timeit("merge_sort(list_one)", setup="from __main__ import merge_sort, list_one", number=tries)
    print("""In an example of the worst case scenario, list two is the reverse of list one: ten thousand to zero in descending order.""" )
    print("""Test runs: 10000
          Average Time = {}""".format(time2 / tries))

