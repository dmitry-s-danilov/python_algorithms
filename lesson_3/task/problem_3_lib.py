def my_func(y):
    """
    Swaps the minimum and maximum elements of an array.

    Parameters:
    y (list): an array to be changed by swapping of minimum and maximum

    Returns:
    tuple: indices of minimum and maximum elements before swapping
    """

    if len(y):
        i = j = 0
        for k in range(1, len(y)):
            if y[k] < y[i]:
                i = k
            elif y[k] > y[j]:
                j = k
        if i != j:
            y[i], y[j] = y[j], y[i]
        return i, j


def my_print(y):
    """
    Prints an enumerated list
    together with its largest and smallest elements

    Parameters:
    y (list): a array to be printed
    """
    for _ in enumerate(y):
        print('{}: {}'.format(*_))
    print(f'min -> {y.index(min(y))}: {min(y)}',
          f'max -> {y.index(max(y))}: {max(y)}',
          sep='\n')
