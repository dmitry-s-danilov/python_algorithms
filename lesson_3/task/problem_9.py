"""
Задача 9
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""

from random import randint
from problem_9_lib import my_func, my_func_2

# set a parameter -
# a matrix of random integers
m, n = 3, 4
r = 1, 100
z = [[randint(*r) for j in range(n)] for i in range(m)]

# find a solution -
# a maximum of matrix column minimums
x = [my_func(z),
     # check
     my_func_2(z)]

# print a report
print(my_func.__name__,
      my_func.__doc__,
      'Parameters:',
      f'matrix: {z}',
      'Returns: ',
      f'maximum of column minimums: {x[0]}',
      f'Check: {x[0] == x[1]}',
      sep='\n')
