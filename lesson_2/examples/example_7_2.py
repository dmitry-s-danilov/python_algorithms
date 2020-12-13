"""
Example 7
Find the greatest common divisor of two integers.
"""


def gcd(m, n):
    while n != 0:
        m, n = n, m % n
    return m


a, b = 21, 27
print(a, b, gcd(a, b))
a, b = 21, 28
print(a, b, gcd(a, b))
a, b = 21, 29
print(a, b, gcd(a, b))
