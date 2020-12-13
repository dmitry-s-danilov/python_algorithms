def my_func(y):
    """
    Finds indices of odd and even elements of a list

    Parameters:
    y (list): a list including integer elements

    Returns:
    tuple: two lists of integers
        those contains indices of odd and even elements respectively

    Examples:
    >>> my_func([8, 3, 15, 6, 4, 2])
    ([1, 2], [0, 3, 4, 5])
    >>> my_func([8, 3, '15', 6, '4', 2])
    ([1], [0, 3, 5])
    """

    i, j = [], []
    for k in range(len(y)):
        try:
            if y[k] % 2:
                i.append(k)
            else:
                j.append(k)
        except TypeError:
            continue
    return i, j
