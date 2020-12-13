"""
Example 7
Find the greatest common divisor of two integers.
"""


def gcd(m, n):
    if n == 0:
        return m
    return gcd(n, m % n)


a, b = 21, 27
print(a, b, gcd(a, b))
a, b = 21, 28
print(a, b, gcd(a, b))
a, b = 21, 29
print(a, b, gcd(a, b))
