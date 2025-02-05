# ZeroDivisionError in Python Average Calculation

This repository demonstrates a common error in Python: the `ZeroDivisionError` that can occur when calculating the average of a list of numbers if the list is empty.

The file `bug.py` contains a function `calculate_average` that fails when given an empty list. The file `bugSolution.py` provides a corrected version that gracefully handles this edge case.

## How to reproduce the bug

1. Run `bug.py`.
2. Observe the `ZeroDivisionError` when the function is called with an empty list. 

## How to fix the bug

The solution involves explicitly checking for an empty list before performing the division. This is done in `bugSolution.py`.