"""Runs three functions calculating the same value,
a sum of array elements.
Measures execution time and checks results to be equal."""

from timeit import timeit
from random import randint
from example_1_lib import *

# set functions to compare:
# create a list of function objects
my_func = my_func_1, my_func_2, my_func_3

# set a common function parameter:
# generate an array of random integers
m = 10
y_range = 1, 100
y = [randint(*y_range) for _ in range(m)]

# set a common timeit parameter:
# a number of executions
n = 100

# find solution and measure execution time for each function:
# generate a dictionary iterating over the list of functions
z = {f.__name__: (f(y), timeit(f'{f.__name__}(y)',
                               number=n,
                               globals=globals()))
     for f in my_func}

# verify solutions:
# check values to be equal
# while iterating over the list of received values
v = [_[0] for _ in z.values()]
c = all([_ == v[0] for _ in v[1:]])

# print a report
z_row = '{} | {} | {}'
z_table = z_row.format('functions', 'returns', 'time')
for f, u in z.items():
    z_table += '\n' + z_row.format(f, *u)
print(my_func[0].__name__,
      my_func[0].__doc__,
      f'length: {m}',
      f'array: {y}',
      f'executions: {n}',
      z_table,
      f'check: {c}',
      sep='\n')
