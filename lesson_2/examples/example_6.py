"""
Example 6
Find the greatest common divisor of two integers.
"""


def gcd(m, n):
    while n != m:
        if m < n:
            n -= m
        else:
            m -= n
    return m


a, b = 21, 27
print(a, b, gcd(a, b))
a, b = 21, 28
print(a, b, gcd(a, b))
a, b = 21, 29
print(a, b, gcd(a, b))

a, b = 37, 43
print(a, b, gcd(a, b))
a, b = 43, 37
print(a, b, gcd(a, b))
