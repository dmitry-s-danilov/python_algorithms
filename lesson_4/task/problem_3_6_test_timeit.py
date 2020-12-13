"""
Timeit tests
============

Using command line interface provided by *timeit* module,
measures execution time of module *problem_3_6_lib* functions:

- *my_func_1*
- *my_func_2*

Herewith uses as an argument of testing functions
an array of random integers *v*
generated with parameters:

- a random range *r*
- array length *n*

Cases
=====

Case 1
------

set parameters:
    .. code-block:: python

    r, n = (1, 100), 10

run *timeit* for *my_func_1*:
    .. code-block:: bash

    python3 -m timeit --number=1000 --repeat=10 \
    --setup='from problem_3_6_lib import my_func_1; \
    from problem_3_6_test_timeit import v' \
    'my_func_1(v)'

    1000 loops, best of 10: 3.6 usec per loop

my_func_2:
    .. code-block:: bash

    python3 -m timeit --number=1000 --repeat=10 \
    --setup='from problem_3_6_lib import my_func_2; \
    from problem_3_6_test_timeit import v' \
    'my_func_2(v)'

    1000 loops, best of 10: 2.36 usec per loop

Case 2
------

params:
    .. code-block:: python

    r, n = (1, 1000), 100

my_func_1:
    .. code-block:: bash

    python3 -m timeit --number=1000 --repeat=10 \
    --setup='from problem_3_6_lib import my_func_1; \
    from problem_3_6_test_timeit import v' \
    my_func_1(v)'

    1000 loops, best of 10: 27.8 usec per loop

my_func_2:
    .. code-block:: bash

    python3 -m timeit --number=1000 --repeat=10 \
    --setup='from problem_3_6_lib import my_func_2; \
    from problem_3_6_test_timeit import v' \
    'my_func_2(v)'
    1000 loops, best of 10: 10.5 usec per loop

Case 3
------

params:
    .. code-block:: python

    r, n = (1, 10000), 1000

my_func_1:
    .. code-block:: bash

    python3 -m timeit --number=1000 --repeat=10 \
    --setup='from problem_3_6_lib import my_func_1; \
    from problem_3_6_test_timeit import v' \
    'my_func_1(v)'
    1000 loops, best of 10: 341 usec per loop

tmy_func_2:
    .. code-block:: bash

    python3 -m timeit --number=1000 --repeat=10 \
    --setup='from problem_3_6_lib import my_func_2; \
    from problem_3_6_test_timeit import v' \
    'my_func_2(v)'

    1000 loops, best of 10: 99.8 usec per loop

Results
=======

+-------+--------+-----------+-----------+
| range | number | my_func_1 | my_func_1 |
+=======+========+===========+===========+
|   100 |     10 |  3.6 usec | 2.36 usec |
+-------+--------+-----------+-----------+
|  1000 |    100 | 27.8 usec | 10.5 usec |
+-------+--------+-----------+-----------+
| 10000 |   1000 |  341 usec | 99.8 usec |
+-------+--------+-----------+-----------+
"""

from random import randint

# set a random range and array length
r, n = (1, 100), 10
# generate an array of random integers
v = [randint(*r) for _ in range(n)]
