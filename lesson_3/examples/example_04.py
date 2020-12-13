"""
Example 4
One item tuple syntax
"""

# a tuple of three items
x = ('one', 'two', 'three')
print(x,
      f'type: {type(x)}',
      f'length: {len(x)}',
      sep='\n')
for _ in enumerate(x):
    print('{}: {}'.format(*_))

print()

# a tuple of two items
x = ('one', 'two')
print(x,
      f'type: {type(x)}',
      f'length: {len(x)}',
      sep='\n')
for _ in enumerate(x):
    print('{}: {}'.format(*_))

print()

# a string, not a tuple
x = ('one')
print(x,
      f'type: {type(x)}',
      f'length: {len(x)}',
      sep='\n')
for _ in enumerate(x):
    print('{}: {}'.format(*_))

print()

# a tuple of one item
x = ('one',)
print(x,
      f'type: {type(x)}',
      f'length: {len(x)}',
      sep='\n')
for _ in enumerate(x):
    print('{}: {}'.format(*_))
