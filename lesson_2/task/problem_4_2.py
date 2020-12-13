"""
Problem 4
Find the sum of geometric progression items

Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры.
"""

b, q = 1, -.5
n = int(input('input items number: '))

s = 0
for k in range(1, n + 1):
    s += q ** (k - 1)
s *= b

print(f'sum: {s}')
