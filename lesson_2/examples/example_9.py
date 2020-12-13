"""
Example 9
Decimal to binary conversion.
"""


def binary(n):
    s = ''
    while n:
        s = str(n % 2) + s
        n //= 2
    return s


while True:
    m = int(input('input integer number: '))
    if m:
        print(f'binary: {binary(m)}')
    else:
        break
