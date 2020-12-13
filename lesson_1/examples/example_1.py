"""
Example 1
Find the quotient of the division of two real numbers.
"""

print('to find the quotient',
      'input two real numbers')

a = float(input('input dividend:'))
b = float(input('input divisor:'))

if b != 0:
    c = a / b
    print(f'quotient: {c}')
else:
    print('no solution')
