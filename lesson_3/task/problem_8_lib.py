def my_func(m, n):
    """
    Fills a matrix of specified size with input,
    except the last row items,
    after that сalculates the sum of row elements
    and append it to the last item of the row.

    Parameters:
    m (int): a number of rows
    n (int): a number of columns

    Returns:
    list: a matrix whose last column contains a sums of row items
    """

    z = []
    for i in range(m):
        y = []
        s = 0
        for j in range(n - 1):
            x = float(input(f'({i}, {j}): '))
            y.append(x)
            s += x
        y.append(s)
        z.append(y)
        print(f'({i}, {n - 1}): {s} [row sum]')
    return z


def my_print(z):
    """
    Prints a 2D array in matrix style.

    Parameters:
    z(list): a 2D array to be displayed
    """
    m, n = len(z), len(z[0])
    for i in range(m):
        for j in range(n):
            print(z[i][j], end=' ')
        print()
