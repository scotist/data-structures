"""Implement quicksort algorithm."""
# import timeit


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
    from time_sorting import time_sorting
    time_sorting(quick_sort)
