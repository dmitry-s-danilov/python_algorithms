"""
Задача 3
В массиве случайных целых чисел
поменять местами минимальный и максимальный элементы.
"""

from random import randint
from problem_3_lib import my_func, my_print

# set a parameter -
# an array of random integers
n = 10
r = 1, 100
y = [randint(*r) for _ in range(n)]

# print a call
print(my_func.__name__,
      my_func.__doc__,
      sep='\n')

# print initial array
print('random:')
my_print(y)

# change the array -
# swap minimum and maximum
print('\n{}: {} <-> {}\n'.format(my_func.__name__, *my_func(y)))

# print changed array
print('swapped:')
my_print(y)
