"""
Problem 3
Generate from the input natural number the reverse in the order of its digits

Сформировать из введенного числа обратное по порядку входящих в него цифр
и вывести на экран.
Например, если введено число 3486, надо вывести 6843.
"""

n = int(input('input natural number: '))

s = ''
while n:
    s += str(n % 10)
    n //= 10

print(f'reverse: {s}')
