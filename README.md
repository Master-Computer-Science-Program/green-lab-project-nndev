# green-lab-project

## Guidelines

| Family          | Guideline | Description |
|-----------------|-----------|-------------|
| Code Optimization | G1  | When there are multiple occurrences of the same expression, assign it to a variable and use the variable. |
|                 | G2  | Avoid redundant operations in sorting already sorted or semi-sorted collections. |
|                 | G3  | Use loop optimization techniques (e.g., loop unrolling, loop unswitching, early termination) to improve performance, such as storing the loop end condition in a variable. |
|                 | G4  | Use short-circuit versions of logical operators where the second argument of a logical expression is evaluated only if the first argument is insufficient to determine the value of the expression. |
|                 | G5  | When high-precision computation is not needed, use approximate computations. |
|                 | G6  | Avoid storing or saving data that has already been computed, saved, or is unnecessary. For example, don't recompute data that is available in a local variable, or avoid having variables only for debugging purposes. |
| Function Calls  | G18 | Use memoization to avoid repeated execution of expensive pure functions. |
|                 | G19 | Reduce function calls to minimize overhead; use static methods and inline code to avoid lookup delays. |


## Run Code

### Installation

- Python version 3.11
- Install packages: `pip3 install -r requirements.txt`

### Run experiment
