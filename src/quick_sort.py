"""Implement quicksort algorithm."""
import timeit


def quick_sort(your_list):
    """Quick sort algorithm using list comprehensions."""
    if your_list == []:
        return []
    else:
        pivot = your_list[0]
        smaller = quick_sort([x for x in your_list[1:] if x < pivot])
        larger = quick_sort([x for x in your_list[1:] if x >= pivot])
        return smaller + [pivot] + larger


if __name__ == "__main__":
    list_one = list(range(990))
    tries = 10000
    time1 = timeit.timeit("quick_sort(list_one)", setup="from __main__ import quick_sort, list_one", number=tries)
    print("""Best case scenario for quick sort algorithm:
          list one is a list of all the integers from one to ten thousand in ascending order.""".format(time1))
    print("""Test runs: 10000
          Average Time = {}""".format(time1 / tries))

    list_two = list(range(990))
    list_two.reverse()
    time2 = timeit.timeit("quick_sort(list_one)", setup="from __main__ import quick_sort, list_one", number=tries)
    print("""In an example of the worst case scenario, list two is the reverse of list one: ten thousand to zero in descending order.""" )
    print("""Test runs: 10000
          Average Time = {}""".format(time2 / tries))