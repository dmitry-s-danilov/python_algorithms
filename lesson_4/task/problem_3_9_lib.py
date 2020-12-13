"""Задача 3.9
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""

def my_func(z):
    """
    Finds the maximum element
    among the minimum elements of the matrix columns

    Parameters:
    z (list): a matrix of numbers

    Returns:
    num: a maximum of column minimums
    """

    m, n = len(z), len(z[0])
    y = z[0]
    for i in range(1, m):
        for j in range(n):
            if z[i][j] < y[j]:
                y[j] = z[i][j]
    x = y[0]
    for i in range(1, n):
        if y[i] > x:
            x = y[i]
    return x


def my_func_2(z):
    m, n = len(z), len(z[0])
    w = [[z[i][j] for i in range(m)] for j in range(n)]
    v = [min(*w[i]) for i in range(n)]
    u = max(*v)
    return u
