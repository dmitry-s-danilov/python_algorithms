from example_09 import insert

# set an item and a list
x = 'x'
y = list(range(10))

# try to insert an item into an array at all positions
for _ in range(len(y) + 1):
    z = y[:]
    print(f'{insert(z, x, _):>2d}: {z}')
