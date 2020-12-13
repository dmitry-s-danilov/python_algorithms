"""
Exaample 9
Insert an element into an array
"""


def insert(array, item, position):
    array.append(None)
    index = len(array) - 1
    while index > position:
        array[index] = array[index - 1]
        index -= 1
    array[index] = item
    return index
