"""
Problem 2
Count the even and odd digits of the input natural number

Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560,
в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""

n = int(input('input natural number: '))

e, o = 0, 0
while n:
    k = n % 2
    if k:
        o += 1
    else:
        e += 1
    n //= 10

print(f'even digits: {e}\nodd digits: {o}')
