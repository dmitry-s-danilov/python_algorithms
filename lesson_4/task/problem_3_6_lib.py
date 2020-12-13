"""Задание 3. Задача 6

В одномерном массиве найти сумму элементов,
находящихся между минимальным и максимальным элементами,
при этом сами минимальный и максимальный элементы в сумму не включать.
"""


def my_func_1(y):
    """
    Finds the sum of numeric array items
    between the minimum and maximum elements,
    excluding themselves.

    :param y: a numeric array
        is for to calculate the sum of items
        between the maximum and minimum elements excluding
    :type y: list

    :return: a sum of array items
        between the minimum and maximum elements excluding
    :rtype: numeric

    :Examples:

    >>> my_func_1([1, 2, 3, 4])
    5
    >>> my_func_1([2, 1, 3, 4])
    3
    >>> my_func_1([2, 3, 1, 4])

    >>> my_func_1([2, 3, 4, 1])

    >>> my_func_1([3, 2, 4, 1])

    >>> my_func_1([3, 4, 2, 1])
    2
    >>> my_func_1([4, 3, 2, 1])
    5
    """

    i, j = 0, 0  # indices of minimum and maximum
    for k in range(1, len(y)):
        if y[k] < y[i]:
            i = k
        elif y[k] > y[j]:
            j = k
    if abs(i - j) > 1:
        r = (i + 1, j) if i < j else (j + 1, i)
        s = 0
        for k in range(*r):
            s += y[k]
        return s


def my_func_2(y):
    i, j = y.index(min(y)), y.index(max(y))
    if abs(i - j) > 1:
        return sum(y[i + 1:j] if i < j else y[j + 1: i])


def my_test(f):
    w = {(0, 0): None,
         (0, 1): None,
         (1, 0): None,
         (1, 1): None,

         (0, 0, 0): None,

         (1, 0, 0): None,
         (0, 1, 0): None,
         (0, 0, 1): 0,

         (0, 1, 1): None,
         (1, 0, 1): None,
         (1, 1, 0): 1,

         (1, 1, 1): None,

         (0, 1, 2): 1,
         (2, 0, 1): None,
         (1, 2, 0): None,

         (2, 1, 0): 1,
         (0, 2, 1): None,
         (1, 0, 2): None,

         (0, 1, 2, 3): 3,
         (1, 0, 2, 3): 2,
         (1, 2, 0, 3): None,
         (1, 2, 3, 0): None,
         (2, 1, 3, 0): None,
         (2, 3, 1, 0): 1,
         (3, 2, 1, 0): 3}
    for u, v in w.items():
        assert v == f(list(u))
