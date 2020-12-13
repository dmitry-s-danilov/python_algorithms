"""
Example 1
Delete list items during iteration
"""

# list length
n = 10

# use del operator
x = list(range(n))
for _ in x:
    # break the connection between the variable and the object
    # to which this variable links
    del _
print(x)

# use remove method
x = list(range(n))
for _ in x:
    # when an element is removed,
    # the loop pointer displaces
    x.remove(_)
print(x)

# use pop method
# which works like to remove one
x = list(range(n))
for _ in enumerate(x):
    # when an element is poped,
    # the loop pointer displaces
    x.pop(_[0])
print(x)

# use remove method
# while iterating over a copy
x = list(range(n))
for _ in x[:]:
    x.remove(_)
print(x)
