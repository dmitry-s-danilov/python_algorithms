"""
Задача 8
Матрица 5x4 заполняется вводом с клавиатуры,
кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки
и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""

from problem_8_lib import my_func, my_print

# set a parameters -
# numbers of row and columns
m, n = 5, 4

# print call
print(my_func.__name__,
      my_func.__doc__,
      'Parameters:',
      f'rows: {m}',
      f'columns: {n}',
      'Fill:',
      sep='\n')

# fill a matrix
z = my_func(m, n)

# print result
print('Returns:')
my_print(z)
