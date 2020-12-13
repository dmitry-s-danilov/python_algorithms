"""
Example 4.1
Find the maximum of three real numbers.
"""

x = float(input('input x: '))
y = float(input('input y: '))
z = float(input('input z: '))

m = x

if m < y:
    m = y

if m < z:
    m = z

print(f'maximum: {m}')
