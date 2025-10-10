"""
A pure Python implementation of the quick sort algorithm

For doctests run following command:
python3 -m doctest -v quick_sort.py

For manual testing run:
python3 quick_sort.py
"""

from __future__ import annotations
from benchmarks.G2.config import C8_ARG
from random import randrange
import time

def quick_sort(collection: list) -> list:
    """A pure Python implementation of quicksort algorithm.

    :param collection: a mutable collection of comparable items
    :return: the same collection ordered in ascending order

    Examples:
    >>> quick_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> quick_sort([])
    []
    >>> quick_sort([-2, 5, 0, -45])
    [-45, -2, 0, 5]
    """
    # Base case: if the collection has 0 or 1 elements, it is already sorted
    if len(collection) < 2:
        return collection

    # Randomly select a pivot index and remove the pivot element from the collection
    pivot_index = randrange(len(collection))
    pivot = collection.pop(pivot_index)

    # Partition the remaining elements into two groups: lesser or equal, and greater
    lesser = [item for item in collection if item <= pivot]
    greater = [item for item in collection if item > pivot]

    first_sort = [*quick_sort(lesser), pivot, *quick_sort(greater)]

    # # Recursively sort the lesser and greater groups, and combine with the pivot
    # return [*quick_sort(lesser), pivot, *quick_sort(greater)]

    #SORT AGAIN
    pivot_index_second = randrange(len(first_sort))
    pivot_second = first_sort.pop(pivot_index_second)

    # Partition the remaining elements into two groups: lesser or equal, and greater
    lesser_second = [item for item in first_sort if item <= pivot_second]
    greater_second = [item for item in first_sort if item > pivot_second]

    return [*quick_sort(lesser_second), pivot_second, *quick_sort(greater_second)]


if __name__ == "__main__":
    n = 300000000
    start_time = time.time()

    for _ in range(n):
        quick_sort(C8_ARG)

    end_time = time.time()
    total_time = end_time - start_time
    print(f"Executed quick_sort {n} times.")
    print(f"Total execution time: {total_time:.6f} seconds")
    print(f"Average execution time per run: {total_time / n:.6f} seconds")