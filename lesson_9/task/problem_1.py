"""Задача 1

Определение количества различных подстрок
с использованием хеш-функции.
Пусть на вход функции дана строка.
Требуется вернуть количество различных подстрок в этой строке.

Примечания:
- в сумму не включаем пустую строку и строку целиком
- без использования функций для вычисления хэша
  `hash()`, `sha1()` или любой другой из модуля `hashlib`
  задача считается не решённой."""

from problem_1_func import func_3

while True:
    s = input('input string: ').strip()
    if len(s) > 0:
        try:
            print(f'substrings: {func_3(s)}')
        except AssertionError:
            print('The string must contain more than one character.')
            continue
    else:
        break
