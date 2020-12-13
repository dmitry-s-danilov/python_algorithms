"""
Example 2
Input a real number in the specified range (post-condition loop).
"""

a, b = 0, 100
while True:
    x = float(input(f'input a number between {a} and {b}: '))
    if a <= x <= b:
        break
