"""
Problem 1
Addition, subtraction, multiplication and division of two real numbers

Написать программу, которая будет складывать, вычитать,
умножать или делить два числа.
Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не завершается,
а запрашивает новые данные для вычислений.
Завершение программы должно выполняться
при вводе символа '0' в качестве знака операции.
Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
программа должна сообщать об ошибке и снова запрашивать знак операции.
Также она должна сообщать пользователю о невозможности деления на ноль,
если он ввел его в качестве делителя.
"""

a, s, m, d, e = '+', '-', '*', '/', '0'
print(f'to operate input:',
      f'[{a}] addition',
      f'[{s}] subtraction',
      f'[{m}] multiplication',
      f'[{d}] division',
      f'[{e}] exit',
      sep='\n')

while True:
    c = input('input operator: ').strip()
    if c in (a, s, m, d):
        x = float(input('input first argument: '))
        y = float(input('input second argument: '))
        if c == a:
            z = x + y
        elif c == s:
            z = x - y
        elif c == m:
            z = x * y
        else:
            if y:
                z = x / y
            else:
                print('invalid argument: zero division')
                continue
        print(f'{x:.2f} {c} {y:.2f} = {z:.2f}')
        continue
    elif c == '0':
        break
    else:
        print('invalid operator')
