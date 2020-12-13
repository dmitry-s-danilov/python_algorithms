"""Measures execution time
of specified function
for different argument values
with timeit module using callable.
"""

from example_2_lib_test import test_time, test_time_table
from example_2_lib_fib import fib_1

func = fib_1  # function
params = [0, 1, 2, 3, 4, 5, 10]  # arguments list
number = 1000  # executions number
time_factor = 10**3  # time factor: converts msec to usec

table = test_time_table(test_time(func=func,
                                  params=params,
                                  number=number,
                                  globs=globals()),
                        time_factor=time_factor)

print(f'function: {func.__name__}',
      f'executions number: {number}',
      f'time factor: {time_factor}',
      table,
      sep='\n')
