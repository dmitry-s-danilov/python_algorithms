"""
Problem 4
Find the sum of geometric progression items

Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры.
"""

b, q = 1, -.5
n = int(input('input items number: '))

k, s = 1, b
while k < n:
    b *= q
    s += b
    k += 1

print(f'sum: {s}')
