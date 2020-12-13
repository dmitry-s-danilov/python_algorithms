"""Apply self test to specified functions."""

from example_2_lib_fib import *

test = test_fib
funcs = fib_1, fib_1_faulty, fib_1_memo,\
        fib_2, fib_3, fib_4

tests = dict()
for func in funcs:
    check = True
    try:
        test(func)
    except AssertionError:
        check = False
    finally:
        tests[func.__name__] = check

row = '{} | {}'
table = row.format('func', 'test')
for _ in tests.items():
    table += '\n' + row.format(*_)

print(f'test: {test.__name__}', table, sep='\n')
