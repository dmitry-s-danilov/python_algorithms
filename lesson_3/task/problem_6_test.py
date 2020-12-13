from doctest import run_docstring_examples
from problem_6_lib import my_func

run_docstring_examples(my_func, globals().copy(), verbose=True,
                       name=f'{my_func.__name__} docstring')
