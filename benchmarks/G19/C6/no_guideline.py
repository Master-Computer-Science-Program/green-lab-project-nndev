import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config 
import time

def and_gate(input_1: int, input_2: int) -> int:
    """
    Calculate AND of the input values

    >>> and_gate(0, 0)
    0
    >>> and_gate(0, 1)
    0
    >>> and_gate(1, 0)
    0
    >>> and_gate(1, 1)
    1
    """
    return int(input_1 and input_2)


def n_input_and_gate(inputs: list[int]) -> int:
    """
    Calculate AND of a list of input values

    >>> n_input_and_gate([1, 0, 1, 1, 0])
    0
    >>> n_input_and_gate([1, 1, 1, 1, 1])
    1
    """
    return int(all(inputs))


if __name__ == "__main__":
    looper=config.C6_ARG
    for i in looper:
        if len(i)==2:
            print(and_gate(i[0],i[1]))
        else:
            print(n_input_and_gate(i))