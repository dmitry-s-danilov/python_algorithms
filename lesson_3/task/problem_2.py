"""
Задача 2
Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
второй массив надо заполнить значениями 0, 3, 4, 5.
"""

from random import randint, choices
from problem_2_lib import my_func

# set a parameter -
# an array of random integers
n = 20
r = 0, 100
y = [randint(*r) for _ in range(n)]

# spoil the array
# by insert of another type elements
v = [None, '', []]
k = choices(list(range(len(v))), k=len(v))
for _ in range(len(v)):
    y[k[_]] = v[_]

# find a solution -
# indices of odd and even elements of the array
i, j = my_func(y)

# print a report
print(my_func.__name__,
      my_func.__doc__,
      'Parameters:',
      f'array: {y}',
      'Returns:',
      f'indices of odds: {i}',
      f'indices of evens: {j}',
      'Check:',
      sep='\n')

# print the array
print(f'array: {len(y)}')
for _ in enumerate(y):
    print('{}: {}'.format(*_))

# print the array of indices of odds
print(f'odds: {len(i)}')
for _ in i:
    print(f'{_}: {y[_]}')

# print the array of indices of evens
print(f'evens: {len(j)}')
for _ in j:
    print(f'{_}: {y[_]}')
