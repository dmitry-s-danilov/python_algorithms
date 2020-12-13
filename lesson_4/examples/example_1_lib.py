"""There are three functions calculating the same value,
a sum of array elements."""

from functools import reduce


def my_func_1(y):
    """returns a sum of array elements

    :param y: an array of numbers whose sum should be calculated
    :type y: list,...
    :returns: a sum of array elements
    :rtype: int, float,...

    :Example:
    >>> my_func_1([1, 2, 3])
    6
    >>> my_func_1(range(0, 10))
    45

    """
    s = 0
    for x in y:
        s += x
    return s


def my_func_2(y):
    return reduce(lambda a, b: a + b, y)


def my_func_3(y):
    return sum(y)
