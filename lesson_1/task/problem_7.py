"""
Problem 7
Check whether the year is a leap one.

Определить, является ли год, который ввел пользователь,
високосным или не високосным.

Examples:
1600 -> a leap
1700 -> not a leap
1800 -> not a leap
1900 -> not a leap
2000 -> a leap

2020 -> a leap
2021 -> not a leap
2022 -> not a leap
2023 -> not a leap
2024 -> a leap
"""

year = int(input('input year: '))

if year % 100 == 0:
    if year % 400 == 0:
        print(f'{year} is a leap year')
    else:
        print(f'{year} is a not leap year')
else:
    if year % 4 == 0:
        print(f'{year} is a leap year')
    else:
        print(f'{year} is a not leap year')
