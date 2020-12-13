from timeit import timeit


def test_time(func, params, number, globs):
    return {param: (func(param),
                    timeit(f'{func.__name__}({param})',
                           number=number,
                           globals=globs))
            for param in params}


def test_time_table(tests, time_factor):
    row = '{} | {} | {}'
    table = row.format('param', 'result', 'time')
    for param, value in tests.items():
        result, time = value
        time = time * time_factor
        time = f'{time:.3f}'
        table += '\n' + row.format(param, result, time)
    return table
