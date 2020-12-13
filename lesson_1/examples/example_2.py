"""
Example 2
Find the sum and product of digits of a three-digit integer number.
"""

print('to find sum and product of digits',
      'input a three-digit integer number')

n = int(input('input integer number:'))

x = n // 100
y = n % 100 // 10
z = n % 10

s = x + y + z
p = x * y * z

print(f'{x} + {y} + {z} = {s}',
      f'{x} * {y} * {z} = {p}',
      sep='\n')
