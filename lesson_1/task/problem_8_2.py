"""
Problem 8
Find the average of three different real numbers.

Вводятся три разных числа.
Найти, какое из них является средним (больше одного, но меньше другого).

Examples:
a = 1, b = 2, c = 3 -> minimum = 1, average = 2, maximum = 3
a = 2, b = 3, c = 1 -> minimum = 1, average = 2, maximum = 3
a = 3, b = 1, c = 2 -> minimum = 1, average = 2, maximum = 3
a = 3, b = 2, c = 1 -> minimum = 1, average = 2, maximum = 3
a = 2, b = 1, c = 3 -> minimum = 1, average = 2, maximum = 3
a = 1, b = 3, c = 2 -> minimum = 1, average = 2, maximum = 3

a = 1, b = 1, c = 1 -> minimum = 1, average = 1, maximum = 1

a = 1, b = 1, c = 2 -> minimum = 1, average = 1, maximum = 2
a = 1, b = 2, c = 1 -> minimum = 1, average = 1, maximum = 2
a = 2, b = 1, c = 1 -> minimum = 1, average = 1, maximum = 2

a = 1, b = 2, c = 2 -> minimum = 1, average = 2, maximum = 2
a = 2, b = 1, c = 2 -> minimum = 1, average = 2, maximum = 2
a = 2, b = 2, c = 1 -> minimum = 1, average = 2, maximum = 2
"""

a = float(input('input a: '))
b = float(input('input b: '))
c = float(input('input c: '))

if a < b:
    minimum = a
    maximum = b
else:
    minimum = b
    maximum = a

if maximum < c:
    average = maximum
    maximum = c
elif c < minimum:
    average = minimum
    minimum = c
else:
    average = c

print(f'minimum: {minimum}',
      f'average: {average}',
      f'maximum: {maximum}',
      sep='\n')
