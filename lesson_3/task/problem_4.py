"""
Задача 4
Определить, какое число в массиве встречается чаще всего.
"""

from random import randint
from problem_4_lib import my_func_1, my_func_2

# set a parameter -
# an array of random integers in specified range
n = 20
r = 1, 10
y = [randint(*r) for _ in range(n)]

# solve a problem
v = my_func_1(y)
x, k = my_func_2(v, lambda a, b: a > b)

# print a report
print(f'random: {y}',
      f'frequencies: {v}',
      f'most frequent: {x} - frequency: {k}',
      sep='\n')
