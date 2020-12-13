"""Implements several variants of the Fibonacci sequence
with the aim to practice timeit and cProfile modules."""

from functools import lru_cache


def test_fib(func):
    """checks Fibonacci sequence function

    Checks the first 12 numbers of the sequence given by the function
    to be equal to the members of the Fibonacci sequence.
    """
    fib_l = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    for n, a in enumerate(fib_l):
        assert a == func(n)


def fib_1(n):
    """returns Fibonacci sequence member

    Recursion is used.

    :param n: non-negative integer sequence member number
    :type n: int
    :return: sequence member
    :rtype: int

    :Example:

    >>> fib_1(0)
    0
    >>> fib_1(1)
    1
    >>> fib_1(2)
    1
    >>> fib_1(3)
    2
    >>> fib_1(4)
    3
    """
    if n < 2:
        return n
    return fib_1(n - 2) + fib_1(n - 1)


@lru_cache()
def fib_1_memo(n):
    """returns Fibonacci sequence member

    Recursion is used together with memoization decorator.

    :param n: non-negative integer sequence member number
    :type n: int
    :return: sequence member
    :rtype: int

    .. note:: fib_1_memo(n) is a memoized clone of fib_1(n)
    """
    if n < 2:
        return n
    return fib_1(n - 2) + fib_1(n - 1)


def fib_1_faulty(n):
    """returns faulty Fibonacci sequence member

    Recursion is used.
    Returns sequence member,
    which is one more than the Fibonacci sequence one.

    :param n: non-negative integer sequence member number
    :type n: int
    :return: sequence member
    :rtype: int

    .. note:: fib_1_faulty(n) is a faulty clone of fib_1(n)
        to check test_fib(func)
    """
    if n < 2:
        return n
    return fib_1(n - 2) + fib_1(n - 1) + 1


def fib_2(n):
    """returns Fibonacci sequence member

    Recursion and dictionary-based memoization is used.

    :param n: non-negative integer sequence member number
    :type n: int
    :return: sequence member
    :rtype: int
    """
    fib_d = {0: 0, 1: 1}

    def _fib_2(k: int):
        if k not in fib_d:
            fib_d[k] = fib_2(k - 2) + fib_2(k - 1)
        return fib_d[k]

    return _fib_2(n)


def fib_3(n):
    """returns Fibonacci sequence member

    Recursion and list-based memoization is used.

    :param n: non-negative integer sequence member number
    :type n: int
    :return: sequence member
    :rtype: int
    """
    # it is supposed to use an array of limited length
    fib_l = 1000 * [None]
    fib_l[:2] = [0, 1]

    def _fib_3(k: int):
        if fib_l[k] is None:
            fib_l[k] = fib_3(k - 2) + fib_3(k - 1)
        return fib_l[k]

    return _fib_3(n)


def fib_4(n):
    """returns Fibonacci sequence member

    No memoization. Simple loop is used.

    :param n: non-negative integer sequence member number
    :type n: int
    :return: sequence member
    :rtype: int
    """
    if n < 2:
        return n
    k = [0, 1]
    for _ in range(2, n + 1):
        k[:2] = [k[-1], k[-2] + k[-1]]
    return k[-1]
