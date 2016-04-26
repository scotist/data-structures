"""Time how long a sorting algorithm takes."""
import timeit


def time_sorting(algo):
    """Print results when checking the time."""
    size = 990
    tries = 10000
    list_one = list(range(size))
    time1 = timeit.timeit(lambda: algo(list_one), number=tries)
    print("""
        Best case scenario: all integers 0-989 in ascending order.
        {} algorithm
        Test runs: {}
        Total time: {}
        Average Time: {}
        """.format(algo.__name__, tries, time1, time1 / tries))

    list_two = list(range(size))
    list_two.reverse()
    time1 = timeit.timeit(lambda: algo(list_two), number=tries)
    print("""
        Worst case scenario: all integers 0-989 in descending order.
        {} algorithm
        Test runs: {}
        Total time: {}
        Average Time: {}
        """.format(algo.__name__, tries, time1, time1 / tries))
