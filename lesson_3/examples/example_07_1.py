from random import randint
from example_07 import binary_search

# set a sorted list of random integers
x_range = 1, 100
x_length = 20
x = [randint(*x_range) for _ in range(x_length)]
x.sort()

# print the list
print('sorted list of {} random integers in the range from {} to {}:'
      .format(x_length, *x_range))
for _ in enumerate(x):
    print('{}: {}'.format(*_))

# run binary search check loop
e = 'exit'
print(f"to check {binary_search.__name__} input integer",
      f"to exit type '{e}'",
      sep='\n')
while True:
    y = input('item: ')
    if y != e:
        y = int(y)
        print(f'position: {binary_search(x, y)}')
    else:
        break
