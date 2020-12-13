"""
Задача 6
В одномерном массиве найти сумму элементов,
находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

from random import shuffle
from problem_6_lib import my_func, my_func_2

# set a parameter -
# an array of shuffled integers from specified range
r = 0, 10
y = list(range(*r))
shuffle(y)

# find a solution -
# a sum of array items
# between the minimum and maximum elements
x = [my_func(y),
     # check
     my_func_2(y)]

# print a report
print(my_func.__name__,
      my_func.__doc__,
      'Parameters:',
      f'array: {y}',
      'Returns: ',
      f'sum between minimum and maximum: {x[0]}',
      f'Check: {x[0] == x[1]}',
      sep='\n')
