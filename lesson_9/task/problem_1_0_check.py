from problem_1_func import *
from problem_1_check import *


# Set parameters.
f_list = [func_1, func_2, func_3]  # functions to be checked
g = func_1  # check function
s_list = ['aa',
          'ab',
          'aaa',
          'aba',
          'abc',
          'aaaaaaaaaaa',
          'abababababa',
          'abcdefghijk',
          'abracadabra']  # string samples
n = 1000  # timeit number

# Apply check.
w = {s: {f.__name__: check(f, g, s, n)
         for f in f_list}
     for s in s_list}

# Print results.
print_check(w, g)
