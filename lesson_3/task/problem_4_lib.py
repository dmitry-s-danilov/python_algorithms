def my_func_1(y):
    """
    Finds the frequency of elements in an array.

    Parameters:
    y (list): an array is for frequency analysis

    Returns:
    dict: a dictionary whose keys are unique elements of the array,
        and the values are their amount in the array
    """

    v = dict()
    for x in y:
        if x in v:
            v[x] += 1
        else:
            v[x] = 1
    return v


def my_func_2(v, c):
    """
    Finds dictionary item
    by sorting item values with specified condition

    Parameter:
    v: a dictionary whose items are for sorted
    c: a binary function which uses as item values sorting condition

    Returns:
    tuple: sorted dictionary item
    """

    x, n = None, 0
    for u, k in v.items():
        if c(k, n):
            x = u
            n = k
    return x, n
