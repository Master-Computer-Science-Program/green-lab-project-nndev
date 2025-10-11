import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config 
import time


def actual_power(a: int, b: int) -> int:
    """
    Function using divide and conquer to calculate a^b.
    It only works for integer a,b.

    :param a: The base of the power operation, an integer.
    :param b: The exponent of the power operation, a non-negative integer.
    :return: The result of a^b.

    Examples:
    >>> actual_power(3, 2)
    9
    >>> actual_power(5, 3)
    125
    >>> actual_power(2, 5)
    32
    >>> actual_power(7, 0)
    1
    """
    if b == 0:
        return 1
    half = actual_power(a, b // 2)

    if (b % 2) == 0:
        return half * half
    else:
        return a * half * half


if __name__ == "__main__":
    start=time.time()
    looper=config.C4_ARG
    for i in looper:
        if(i[1]<0):
            print( 1/actual_power(i[0],-i[1]))
        else:
            print(actual_power(i[0],i[1]))
    end=time.time()
    print(end-start)