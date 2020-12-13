from random import randint

# set a random range and array length
r, n = (1, 100), 10
# generate an array of random integers
v = [randint(*r) for _ in range(n)]

"""
>>> r, n = (1, 100), 10

$ python3 -m timeit --number=1000 --repeat=10 \
> --setup='from problem_3_7_lib import my_func_1; \
> from problem_3_7_test_timeit import v' \
> 'my_func_1(v)'
1000 loops, best of 10: 15.4 usec per loop

$ python3 -m timeit --number=1000 --repeat=10 --unit=usec \
> --setup='from problem_3_7_lib import my_func_2; \
> from problem_3_7_test_timeit import v' \
> 'my_func_2(v)'
1000 loops, best of 10: 0.673 usec per loop

>>> r, n = (1, 1000), 100

$ python3 -m timeit --number=1000 --repeat=10 \
--setup='from problem_3_7_lib import my_func_1; \
from problem_3_7_test_timeit import v' \
'my_func_1(v)'
1000 loops, best of 10: 135 usec per loop

$ python3 -m timeit --number=1000 --repeat=10 --unit=usec \
--setup='from problem_3_7_lib import my_func_2; \
from problem_3_7_test_timeit import v' \
'my_func_2(v)'
1000 loops, best of 10: 6.76 usec per loop

>>> r, n = (1, 10000), 1000

$ python3 -m timeit --number=1000 \
--repeat=10 --setup='from problem_3_7_lib import my_func_1; \
from problem_3_7_test_timeit import v' \
'my_func_1(v)'
1000 loops, best of 10: 1.37 msec per loop

$ python3 -m timeit --number=1000 --repeat=10 --unit=msec \
> --setup='from problem_3_7_lib import my_func_2; \
> from problem_3_7_test_timeit import v' \
'my_func_2(v)'
1000 loops, best of 10: 0.112 msec per loop

| range | number | my_func_1 |  my_func_1 |
+=======+========+===========+============+
|   100 |     10 | 15.4 usec | 0.673 usec |
|  1000 |    100 |  135 usec |  6.76 usec |
| 10000 |   1000 | 1.37 msec | 0.112 msec |
"""
