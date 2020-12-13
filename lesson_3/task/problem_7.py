"""
Задача 7
В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба минимальны), так и различаться.
"""

from functools import partial
from random import randint
from problem_7_lib import my_func, my_func_2

# customize a function
# to correspond the condition of the problem
my_func_1 = partial(my_func,
                    # a growing condition for array ordering
                    c=(lambda a, b: a > b),
                    # a number items from the beginning of an ordered array
                    # to be returned
                    n=2)

# set a parameter -
# an array of random integers to be ordered
n = 10
r = 1, 100
y = [randint(*r) for _ in range(n)]

# find a solution -
# a pair of smallest array elements
x = [my_func_1(y),
     # check
     my_func_2(y)]

# print a report
print(my_func.__name__,
      my_func.__doc__,
      'Parameters:',
      f'array: {y}',
      'Returns: ',
      f'couple of smallest: {x[0]}',
      f'Check: {x[0] == x[1]}',
      sep='\n')
