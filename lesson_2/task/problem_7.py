"""
Problem 7
Verify the sum of natural sequence

Написать программу, доказывающую или проверяющую,
что для множества натуральных чисел выполняется равенство:
1 + 2 + ... + n = n (n+1) / 2, где n — любое натуральное число.
"""

n = int(input('input items number: '))

a, s = n * (n + 1) / 2, 0
for k in range(1, n + 1):
    s += k

print(f'sum: {s} {s == a}')
