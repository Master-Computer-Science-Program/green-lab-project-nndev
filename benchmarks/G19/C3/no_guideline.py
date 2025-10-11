"""
A NOT Gate is a logic gate in boolean algebra which results to 0 (False) if the
input is high, and 1 (True) if the input is low.
Following is the truth table of a XOR Gate:
    ------------------------------
    | Input   |  Output |
    ------------------------------
    |    0    |    1    |
    |    1    |    0    |
    ------------------------------
Refer - https://www.geeksforgeeks.org/logic-gates-in-python/
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config 

def not_gate(input_1: int) -> int:
    """
    Calculate NOT of the input values
    >>> not_gate(0)
    1
    >>> not_gate(1)
    0
    """

    return 1 if input_1 == 0 else 0


if __name__ == "__main__":
    looper=config.C3_ARG
    for i in looper:
        print(not_gate(i))