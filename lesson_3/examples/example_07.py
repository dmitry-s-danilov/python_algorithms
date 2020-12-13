"""
Example 7
Binary search
"""


def binary_search(array, value):
    left, right = 0, len(array) - 1
    central = right // 2
    while value != array[central] and left <= right:
        if value > array[central]:
            left = central + 1
        else:
            right = central - 1
        central = (left + right) // 2
    if left > right:
        central = -1
    return central
