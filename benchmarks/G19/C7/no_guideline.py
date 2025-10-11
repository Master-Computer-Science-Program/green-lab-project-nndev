import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config 
import time

def or_gate(input_1: int, input_2: int) -> int:
    """
    Calculate OR of the input values
    >>> or_gate(0, 0)
    0
    >>> or_gate(0, 1)
    1
    >>> or_gate(1, 0)
    1
    >>> or_gate(1, 1)
    1
    """
    return int((input_1, input_2).count(1) != 0)


if __name__ == "__main__":
    looper=config.C7_ARG
    for i in looper:
        print(or_gate(i[0],i[1]))