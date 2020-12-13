"""
Example 3
Different results with the same operands
"""

x = [1, 2, 3, 4]
y = x
x = x + [5, 6, 7]  # new object creates
print(x, y)

x = [1, 2, 3, 4]
y = x
x += [5, 6, 7]  # existing object modifies
print(x, y)
