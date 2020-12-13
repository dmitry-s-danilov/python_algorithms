from problem_3_7_lib import my_func_1, my_func_2, my_test

funcs = my_func_1, my_func_2
test = my_test

tests = dict()
for func in funcs:
    check = True
    try:
        test(func)
    except AssertionError:
        check = False
    finally:
        tests[func.__name__] = check

row = '{}: {}\n'
table = ''
for _ in tests.items():
    table += row.format(*_)
print(table)
