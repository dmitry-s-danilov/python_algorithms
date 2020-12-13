from doctest import run_docstring_examples
from problem_3_7_lib import my_func

func = my_func
run_docstring_examples(func, globs=globals(), verbose=True,
                       name=f'{func.__name__} docstring examples')
