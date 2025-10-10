"""
This is pure Python implementation of counting sort algorithm
For doctests run following command:
python -m doctest -v counting_sort.py
or
python3 -m doctest -v counting_sort.py
For manual testing run:
python counting_sort.py
"""
from benchmarks.G2.config import C7_ARG
import time

def counting_sort(collection):
    """Pure implementation of counting sort algorithm in Python
    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending
    Examples:
    >>> counting_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> counting_sort([])
    []
    >>> counting_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    # if the collection is empty, returns empty
    if collection == []:
        return []

    # get some information about the collection
    coll_len = len(collection)
    coll_max = max(collection)
    coll_min = min(collection)

    # create the counting array
    counting_arr_length = coll_max + 1 - coll_min
    counting_arr = [0] * counting_arr_length

    # count how much a number appears in the collection
    for number in collection:
        counting_arr[number - coll_min] += 1

    # sum each position with it's predecessors. now, counting_arr[i] tells
    # us how many elements <= i has in the collection
    for i in range(1, counting_arr_length):
        counting_arr[i] = counting_arr[i] + counting_arr[i - 1]

    # create the output collection
    ordered = [0] * coll_len

    # place the elements in the output, respecting the original order (stable
    # sort) from end to begin, updating counting_arr
    for i in reversed(range(coll_len)):
        ordered[counting_arr[collection[i] - coll_min] - 1] = collection[i]
        counting_arr[collection[i] - coll_min] -= 1


    # return ordered - before: return the list right after sorted

    # SORT AGAIN
    # Sort ordered (sorted list) again
    # get some information about the collection
    coll_len_second = len(ordered)
    coll_max_second = max(ordered)
    coll_min_second = min(ordered)

    # create the counting array
    counting_arr_length_second = coll_max_second + 1 - coll_min_second
    counting_arr_second = [0] * counting_arr_length_second

    # count how much a number appears in the collection
    for number in ordered:
        counting_arr_second[number - coll_min_second] += 1

    # sum each position with it's predecessors. now, counting_arr[i] tells
    # us how many elements <= i has in the collection
    for i in range(1, counting_arr_length_second):
        counting_arr_second[i] = counting_arr_second[i] + counting_arr_second[i - 1]

    # create the output collection
    ordered_second = [0] * coll_len_second

    # place the elements in the output, respecting the original order (stable
    # sort) from end to begin, updating counting_arr
    for i in reversed(range(coll_len_second)):
        ordered_second[counting_arr_second[ordered[i] - coll_min_second] - 1] = ordered[i]
        counting_arr_second[ordered[i] - coll_min_second] -= 1

    return ordered_second




def counting_sort_string(string):
    """
    >>> counting_sort_string("thisisthestring")
    'eghhiiinrsssttt'
    """
    return "".join([chr(i) for i in counting_sort([ord(c) for c in string])])


if __name__ == "__main__":
    # Test string sort
    assert counting_sort_string("thisisthestring") == "eghhiiinrsssttt"
    start_time = time.time()
    counting_sort(C7_ARG)
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.6f} seconds") #elapsed time: 71.609513 seconds
    # print(counting_sort(C7_ARG))