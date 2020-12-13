"""Задачи 1

На улице встретились *N* друзей.
Каждый пожал руку всем остальным друзьям (по одному разу).
Сколько рукопожатий было?

Примечание:
решите задачу при помощи построения графа.
"""

from problem_1_lib import *

# Set a list of handshakers numbers.
counts = [0, 1, 2, 3, 6]

# Set a list of pairs of functions
# to generate and process graphs.
funcs = [(func_1, calc_1), (func_2, calc_2), (func_3, calc_3)]

for n in counts:
    print(f'counts: {n}', end='\n\n')
    for func, calc in funcs:
        g = func(n)
        k = calc(g)
        c = k == calc_0(n)

        print(f'{func.__name__}:')

        if hasattr(g, '__iter__'):
            if hasattr(g, 'items'):
                for _ in g.items():
                    print('{}: {}'.format(*_))
            else:
                for _ in enumerate(g):
                    print('{}: {}'.format(*_))
        #         else:
        #             print(g)

        print(f'{calc.__name__}: {k} {c}',
              end='\n\n')
