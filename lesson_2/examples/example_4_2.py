"""
Example 4
Print all integer numbers in specified range (recursion).
"""


def func(a, b):
    if a == b:
        return f'{a}'
    elif a < b:
        return f'{a}, {func(a + 1, b)}'
    return f'{a}, {func(a - 1, b)}'


a, b = 1, 10
print(f'{a}, {b}', func(a, b), sep='\n', end='\n\n')
a, b = 10, 1
print(f'{a}, {b}', func(a, b), sep='\n', end='\n\n')
a, b = 1, 1
print(f'{a}, {b}', func(a, b), sep='\n', end='\n\n')

