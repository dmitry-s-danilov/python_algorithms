"""
Example 3
Find the value of the function depending on the value of the argument.
"""

x = float(input('input x: '))

if x > 0:
    y = 2 * x - 10
else:
    if x == 0:
        y = 0
    else:
        y = 2 * abs(x) - 1

print(f'y: {y}')
