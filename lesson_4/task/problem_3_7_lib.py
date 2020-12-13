"""Задание 3. Задача 7
В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба минимальны), так и различаться.
"""

from functools import partial


def my_func(y, c, n):
    """
    Orders the elements of the array
    in according with the condition defined by the binary operation
    and returns the specified number of elements from the array beginning

    :param y: an array to be ordered
    :param c: a binary operation defining ordering condition
    :param n: a number of ordered array items to be returned
    :type y: list
    :type c: (num, num) -> bool
    :type n: int

    :return:  a specified part from the beginning of an ordered array
    :rtype: list

    Example:

    >>> from random import shuffle
    >>> # create an ascending sequence of numbers
    >>> v = list(range(0, 11))
    >>> # shuffle the members of the sequence
    >>> shuffle(v)
    >>> # sort in descending order
    >>> my_func(v, lambda a, b: a > b, len(v))
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    >>> # find minimum
    >>> my_func(v, lambda a, b: a < b, 1).pop()
    0
    """

    x = [y[0]]
    for i in range(1, len(y)):
        x.append(y[i])
        k = len(x)
        for j in range(-1, -k, -1):
            if not c(x[j - 1], x[j]):
                x[j], x[j - 1] = x[j - 1], x[j]
        if k > n:
            x.pop()
    return x


my_func_1 = partial(my_func, c=lambda a, b: a < b, n=2)
my_func_1.__name__ = 'my_func_1'


def my_func_2(y):
    v = y.copy()
    v.sort()
    return v[:2]


def my_test(f):
    w = {(0, 0): [0, 0],
         (0, 1): [0, 1],
         (1, 0): [0, 1],
         (1, 1): [1, 1],

         (0, 0, 0): [0, 0],

         (1, 0, 0): [0, 0],
         (0, 1, 0): [0, 0],
         (0, 0, 1): [0, 0],

         (0, 1, 1): [0, 1],
         (1, 0, 1): [0, 1],
         (1, 1, 0): [0, 1],

         (1, 1, 1): [1, 1],

         (0, 1, 2): [0, 1],
         (2, 0, 1): [0, 1],
         (1, 2, 0): [0, 1],

         (2, 1, 0): [0, 1],
         (0, 2, 1): [0, 1],
         (1, 0, 2): [0, 1]}
    for u, v in w.items():
        assert v == f(list(u))
