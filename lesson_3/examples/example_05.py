"""
Example 5
Search for unique items in list using set
"""

from random import randint

x_range = 0, 9
x_length = 10 + 1
x = [randint(*x_range) for _ in range(x_length)]
y = list(set(x))
print(f'random: {x}',
      f'unique: {y}',
      sep='\n')
