"""
Example 2
Each element of list is a link on the object
"""

# row and column numbers
m, n = 3, 4

# each main list item links on the same object
x = [0] * n
y = [x] * m
y[0][0] = 1
print(y)

# the same as above
y = [[0] * n] * m
y[0][0] = 1
print(y)

# main list items link on the different objects
y = [[0] * n for _ in range(m)]
y[0][0] = 1
print(y)
