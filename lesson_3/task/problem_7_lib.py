def my_func(y, c, n):
    """
    Orders the elements of the array
    in according with the condition defined by the binary operation
    and returns the specified number of elements from the array beginning

    Parameters:
    y (list): an array to be ordered
    c (func): a binary operation defining ordering condition
    n (int): a number of ordered array items to be returned

    Returns:
    list: a specified part from the beginning of an ordered array
    """

    x = [y[0]]
    for i in range(1, len(y)):
        x.append(y[i])
        k = len(x)
        for j in range(-1, -k, -1):
            if c(x[j - 1], x[j]):
                x[j], x[j - 1] = x[j - 1], x[j]
        if k > n:
            x.pop()
    return x


def my_func_2(y):
    v = y.copy()
    v.sort()
    return v[:2]
