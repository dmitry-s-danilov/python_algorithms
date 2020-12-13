"""
Example 5
Ackermann function (recursion).
"""

from sys import setrecursionlimit


def ack(m, n):
    if m >= 0 and n >= 0:
        if m == 0:
            return n + 1
        elif n == 0:
            return ack(m - 1, 1)
        return ack(m - 1, ack(m, n - 1))


setrecursionlimit(2050)
ack_3 = [ack(3, _) for _ in range(8 + 1)]
for _ in enumerate(ack_3):
    print('{} {}'.format(*_))
