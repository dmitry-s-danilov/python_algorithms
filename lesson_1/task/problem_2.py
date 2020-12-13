"""
Problem 2
Find the equation of the 2D-line using coordinates of two points.

По введенным пользователем координатам двух точек
вывести уравнение прямой вида y = kx + b, проходящей через эти точки.

Examples:
x1 = 0, y1 = 0, x2 = 1, y2 = 1 -> k = 1, b = 0

x1 = 0, y1 = 0, x2 = 2, y2 = 1 -> k = .5, b = 0
x1 = 0, y1 = 0, x2 = .5, y2 = 1 -> k = 2, b = 0

x1 = -1, y1 = 0, x2 = 0, y2 = 1 -> k = 1, b = 1
x1 = 1, y1 = 0, x2 = 2, y2 = 1 -> k = 1, b = -1

x1 = 0, y1 = 1, x2 = 1, y2 = 2 -> k = 1, b = 1
x1 = 0, y1 = -1, x2 = 1, y2 = 0 -> k = 1, b = -1

x1 = 1, y1 = 0, x2 = 1, y2 = 1 -> no solution
x1 = 0, y1 = 1, x2 = 1, y2 = 1 -> k = 0, b = 1
"""

x1 = float(input('input x1: '))
y1 = float(input('input y1: '))
x2 = float(input('input x2: '))
y2 = float(input('input y2: '))

if x1 != x2:
    k = (y2 - y1) / (x2 - x1)
    b = (x2 * y1 - x1 * y2) / (x2 - x1)
    print(f'y = {k:.3f} x + {b:.3f}')
else:
    print('no solution')
