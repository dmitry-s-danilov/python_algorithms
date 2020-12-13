def my_func(y):
    """
    Finds the sum of number array items
    between the minimum and maximum elements,
    excluding the minimum and maximum elements themselves.

    Parameters:
    y (list): a number array
        is for to find the maximum and minimum elements
        and calculate the sum of the items between them

    Returns:
    num: a sum of array items
        between the minimum and maximum elements

    Examples:
    >>> my_func([1, 2, 3])
    2
    >>> my_func([2, 3, 1])

    >>> my_func([3, 1, 2])

    >>> my_func([3, 2, 1])
    2
    >>> my_func([1, 2, 3, 4])
    5
    """

    i, j = 0, 0
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
    i = y.index(min(y))
    j = y.index(max(y))
    if abs(i - j) > 1:
        return sum(y[i + 1:j] if i < j else y[j + 1: i])
