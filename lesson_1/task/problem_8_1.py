"""
Problem 8
Find the average of three different real numbers.

Вводятся три разных числа.
Найти, какое из них является средним (больше одного, но меньше другого).

Examples:
a = 1, b = 2, c = 3 -> average: 2
a = 2, b = 3, c = 1 -> average: 2
a = 3, b = 1, c = 2 -> average: 2
a = 3, b = 2, c = 1 -> average: 2
a = 2, b = 1, c = 3 -> average: 2
a = 1, b = 3, c = 2 -> average: 2

a = 1, b = 1, c = 1 -> average: 1

a = 1, b = 1, c = 2 -> average: 1
a = 1, b = 2, c = 1 -> average: 1
a = 2, b = 1, c = 1 -> average: 1

a = 1, b = 2, c = 2 -> average: 2
a = 2, b = 1, c = 2 -> average: 2
a = 2, b = 2, c = 1 -> average: 2
"""

a = float(input('input a: '))
b = float(input('input b: '))
c = float(input('input c: '))

if a < b:
    if b < c:
        print(f'average: {b}')
    else:
        if a < c:
            print(f'average: {c}')
        else:
            print(f'average: {a}')
else:
    if a < c:
        print(f'average: {a}')
    else:
        if b < c:
            print(f'average: {c}')
        else:
            print(f'average: {b}')
