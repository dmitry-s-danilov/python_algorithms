"""
Задача 1

Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за четыре квартала для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий,
чья прибыль выше среднего и ниже среднего.
"""

from problem_1_lib import f

# Input data.
n = 4  # a number of quarters
m = int(input('input a number of companies: '))

q = dict()
for i in range(m):
    s = input('input a company name: ').strip()
    t = input(f'input a quarter incomes for the year({n}): ')
    t = [float(_) for _ in t.split()[:n]]
    q[s] = t

print('companies quarter incomes for the year:')
for _ in q.items():
    print('{}: {}'.format(*_))


# Solve the problem.
a, b, c = f(q)


# Print results.
k = 2  # rounding accuracy

print(f'average year income: {round(a, k)}')

print(f'companies with lower year income:\n{b}')

for _ in b:
    print(f'{_}: {round(sum(q[_]), k)}')

print(f'companies with higher year income:\n{c}')

for _ in c:
    print(f'{_}: {round(sum(q[_]), k)}')
