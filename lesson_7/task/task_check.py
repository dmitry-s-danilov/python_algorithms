from random import randint, shuffle
from task_func_lib import func_1_0, func_1_1, func_2, func_3
from task_check_lib import func_check, check_string


# Create samples of integers
n = 10  # sample length

y = []

# Create sorted sample.
x = [_ for _ in range(n)]
y.append(x.copy())

# Create unsorted sample
# with no repeating elements.
shuffle(x)
y.append(x.copy())

# Create unsorted sample
# with repeating elements.
r = 0, n - 2
x = [randint(*r) for _ in range(n)]
y.append(x.copy())


# Check functions.
funcs = (func_1_0, func_1_1, func_2, func_3)
checks = [func_check(x, funcs[0], funcs)
          for x in y]

# Print results.
check_fields = ('sample', 'benchmark', 'reference', 'check')

for index, check in enumerate(checks):
    print(index,
          check_string(check, check_fields),
          sep='\n', end='\n\n')
