"""
This is a pure Python implementation of the Cyclic Sort algorithm.

For doctests run following command:
python -m doctest -v cyclic_sort.py
or
python3 -m doctest -v cyclic_sort.py
For manual testing run:
python cyclic_sort.py
or
python3 cyclic_sort.py
"""
import time

from benchmarks.G2.config import C9_ARG

def cyclic_sort(nums: list[int]) -> list[int]:
    """
    Sorts the input list of n integers from 1 to n in-place
    using the Cyclic Sort algorithm.

    :param nums: List of n integers from 1 to n to be sorted.
    :return: The same list sorted in ascending order.

    Time complexity: O(n), where n is the number of integers in the list.

    Examples:
    >>> cyclic_sort([])
    []
    >>> cyclic_sort([3, 5, 2, 1, 4])
    [1, 2, 3, 4, 5]
    """

    # Perform cyclic sort
    index = 0
    while index < len(nums):
        # Calculate the correct index for the current element
        correct_index = nums[index] - 1
        # If the current element is not at its correct position,
        # swap it with the element at its correct index
        if index != correct_index:
            nums[index], nums[correct_index] = nums[correct_index], nums[index]
        else:
            # If the current element is already in its correct position,
            # move to the next element
            index += 1

    #SORT AGAIN
    first_sort = nums
    index_second = 0
    while index_second < len(first_sort):
        # Calculate the correct index for the current element
        correct_index_second = first_sort[index_second] - 1
        # If the current element is not at its correct position,
        # swap it with the element at its correct index
        if index_second != correct_index_second:
            first_sort[index_second], first_sort[correct_index_second] = first_sort[correct_index_second], first_sort[index_second]
        else:
            # If the current element is already in its correct position,
            # move to the next element
            index_second += 1

    return first_sort
if __name__ == "__main__":
    n = 90000000  # Number of repetitions
    param = C9_ARG
    start_time = time.time()

    for _ in range(n):
        cyclic_sort(param)
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Executed cyclic_sort {n} times.")
    print(f"Total execution time: {total_time:.6f} seconds") #79.539053s for 90,000,000 runs