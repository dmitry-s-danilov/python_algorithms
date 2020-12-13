from cProfile import run
from random import randint
from problem_3_7_lib import my_func_2 as f

# set a random range and array length
r, n = (1, 10000), 1000
# generate an array of random integers
v = [randint(*r) for _ in range(n)]

run('f(v)')

"""
>>> r, n = (1, 100), 10

my_func_1: 48 function calls in 0.000 seconds
my_func_2: 6 function calls in 0.000 seconds

>>> r, n = (1, 1000), 100

my_func_1: 498 function calls in 0.003 seconds
my_func_2: 6 function calls in 0.000 seconds

>>> r, n = (1, 10000), 1000

my_func_1:
         4998 function calls in 0.024 seconds

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.024    0.024 <string>:1(<module>)
     1997    0.004    0.000    0.004    0.000 problem_3_7_lib.py:52(<lambda>)
        1    0.014    0.014    0.024    0.024 problem_3_7_lib.py:9(my_func)
        1    0.000    0.000    0.024    0.024 {built-in method builtins.exec}
     1000    0.002    0.000    0.002    0.000 {built-in method builtins.len}
      999    0.002    0.000    0.002    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      998    0.002    0.000    0.002    0.000 {method 'pop' of 'list' objects}

my_func_2:
         6 function calls in 0.000 seconds

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 problem_3_7_lib.py:56(my_func_2)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'copy' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'sort' of 'list' objects}
"""
