"""
Problem 8
Count how many times a certain digit occurs
in the specified sequence of numbers

Посчитать, сколько раз встречается определенная цифра
в введенной последовательности чисел.
Количество вводимых чисел и цифра, которую необходимо посчитать,
задаются вводом с клавиатуры.
"""

m = int(input('input sequence length: '))
d = int(input('input a digit: '))

i = 0
for _ in range(m):
    n = int(input(f'input a number #{_ + 1}:'))
    while n:
        k = n % 10
        if k == d:
            i += 1
        n //= 10

print(f'number of occurrences: {i}')
