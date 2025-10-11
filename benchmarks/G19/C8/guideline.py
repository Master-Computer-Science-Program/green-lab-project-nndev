import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config 
import time


def bin_to_decimal(bin_string: str) -> int:
    """
    Convert a binary value to its decimal equivalent

    >>> bin_to_decimal("101")
    5
    >>> bin_to_decimal(" 1010   ")
    10
    >>> bin_to_decimal("-11101")
    -29
    >>> bin_to_decimal("0")
    0
    >>> bin_to_decimal("a")
    Traceback (most recent call last):
        ...
    ValueError: Non-binary value was passed to the function
    >>> bin_to_decimal("")
    Traceback (most recent call last):
        ...
    ValueError: Empty string was passed to the function
    >>> bin_to_decimal("39")
    Traceback (most recent call last):
        ...
    ValueError: Non-binary value was passed to the function
    """
    neg_flag=0
    bin_string = str(bin_string).strip()
    if not bin_string:
        raise ValueError("Empty string was passed to the function")
    if bin_string[0] == "-":
        bin_string = bin_string[1:]
        neg_flag=1
    if not all(char in "01" for char in bin_string):
        raise ValueError("Non-binary value was passed to the function")
    decimal_number = 0
    for char in bin_string:
        decimal_number = 2 * decimal_number + int(char)
    return -decimal_number if neg_flag else decimal_number


if __name__ == "__main__":
    start=time.time()
    looper=config.C8_ARG
    for i in looper:
        print(i)
        print(bin_to_decimal(i))
    end=time.time()
    print(end-start)