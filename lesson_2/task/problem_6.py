"""
Problem 6.
Guess the integer number

В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться,
больше или меньше введенное пользователем число, чем то, что загадано.
Если за 10 попыток число не отгадано, вывести ответ.
"""

from random import randint

a, b = 0, 100  # random integer range
n = 10  # number of attempts
print(f'guess an integer from {a} to {b} in {n} attempts')

x, g = randint(a, b), False  # random integer and guessing result

for k in range(1, n + 1):
    y = int(input(f'{k}: '))
    if y == x:
        g = True
        break
    elif y > x:
        print('>')
    else:
        print('<')

if g:
    print('=')
else:
    print(x)
