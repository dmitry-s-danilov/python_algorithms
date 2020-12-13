from timeit import timeit


def func_check(u, g, h):
    n = 10000  # timeit numbers

    v = u.copy()
    g(v)

    w = dict()
    for f in h:
        x = u.copy()
        t = timeit('f(x)',
                   number=n,
                   globals=locals())
        s = x == v
        w[f.__name__] = (s, t)

    c = (u, v, g.__name__, w)
    return c


def check_string(c, k):
    s = ''

    for _ in range(len(c) - 1):
        s += f'{k[_]}: {c[_]}\n'

    s += f'{k[-1]}:'

    for p, q in c[-1].items():
        s += '\n\t{}: {} {}'.format(p, *q)
    return s
