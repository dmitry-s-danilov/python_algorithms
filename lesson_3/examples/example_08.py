"""
Example 8
Decompose positive and negative numbers into different arrays
"""


def decompose(array):
    above, below = [], []
    for item in array:
        if item > 0:
            above.append(item)
        elif item < 0:
            below.append(item)
    return above, below
