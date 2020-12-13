"""
Example 6
Using immutable lists and sets as dict keys
"""
x = {1, 2, 3}
y = [1, 2, 3]

# TypeError: unhashable type: 'set'
# z = {x: y}

# TypeError: unhashable type: 'list'
# z = {y: x}

x_frozen = frozenset(x)
z = {x_frozen: y}
print(f'{type(x_frozen)}: {x_frozen}',
      f'{type(y)}: {y}',
      f'{type(z)}: {z}',
      sep='\n', end='\n\n')

y_tuple = tuple(y)
z = {y_tuple: x}
print(f'{type(x)}: {x}',
      f'{type(y_tuple)}: {y_tuple}',
      f'{type(z)}: {z}',
      sep='\n')
