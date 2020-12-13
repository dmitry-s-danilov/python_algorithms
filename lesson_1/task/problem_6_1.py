"""
Problem 6
Check if the numbers are the sides of a non-degenerate triangle
and if such a triangle exists classify it.

По длинам трех отрезков, введенных пользователем,
определить возможность существования треугольника,
составленного из этих отрезков.
Если такой треугольник существует, то определить,
является ли он разносторонним, равнобедренным или равносторонним.

Examples:
a = 1, b = 1, c = 1 -> an equilateral

a = 1, b = 1, c = 2 -> not a triangle

a = 1, b = 2, c = 2 -> an isosceles
a = 2, b = 1, c = 2 -> an isosceles
a = 2, b = 2, c = 1 -> an isosceles

a = 1, b = 2, c = 3 -> not a triangle

a = 2, b = 3, c = 4 -> a scalene
a = 3, b = 4, c = 2 -> a scalene
a = 4, b = 2, c = 3 -> a scalene
a = 4, b = 3, c = 2 -> a scalene
a = 3, b = 2, c = 4 -> a scalene
a = 2, b = 4, c = 3 -> a scalene
"""

a = float(input('input a: '))
b = float(input('input b: '))
c = float(input('input c: '))

if a < b + c and b < c + a and c < a + b:
    if a == b:
        if b == c:
            print('triangle is an equilateral')
        else:
            print('triangle is an isosceles')
    elif b == c:
        print('triangle is an isosceles')
    elif c == a:
        print('triangle is an isosceles')
    else:
        print('triangle is a scalene')
else:
    print('this is not a triangle')
