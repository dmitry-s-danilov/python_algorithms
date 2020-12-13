from timeit import timeit


def check(f, g, s, n):
    u = f(s)
    v = u == g(s)

    w = {'check': v}

    if v:
        t = timeit(stmt='f(s)',
                   number=n,
                   globals=locals())
        t /= n
        w['result'] = u
        w['time'] = t

    return w


def print_check(w, g):
    for s, v in sorted(w.items(),
                       key=(lambda _: _[1][g.__name__]['result'])):

        print(f"string: {s}",
              f"substrings: {v[g.__name__]['result']}",
              sep='\n')

        for f, u in sorted(v.items(),
                           key=(lambda _: _[1]['time'])):

            print(f,
                  u['time'] if u['check'] else u['check'],
                  sep=': ')

        print()
