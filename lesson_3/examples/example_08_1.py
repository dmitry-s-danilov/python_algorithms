from random import randint
from example_08 import decompose

# set a list of random integers
x_range = -100, 100
x_length = 20
x = [randint(*x_range) for _ in range(x_length)]

# print the list
print('list of {} random integers in the range from {} to {}:'
      .format(x_length, *x_range))
for _ in enumerate(x):
    print('{}: {}'.format(*_))

# decompose the list
a, b = decompose(x)

# do the same using list generator
a2 = [_ for _ in x if _ > 0]
b2 = [_ for _ in x if _ < 0]

# check decomposition
print(f'above zero: {len(a)} {a == a2}')
for _ in enumerate(a):
    print('{}: {}'.format(*_))
print(f'above zero: {len(b)} {b == b2}')
for _ in enumerate(b):
    print('{}: {}'.format(*_))


