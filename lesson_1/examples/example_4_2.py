"""
Example 4.2
Find the maximum of three real numbers.
"""

x = float(input('input x: '))
y = float(input('input y: '))
z = float(input('input z: '))

if x < y:
    if y < z:
        print(f'maximum: {z}')
    else:
        print(f'maximum: {y}')
else:
    if x < z:
        print(f'maximum: {z}')
    else:
        print(f'maximum: {x}')
