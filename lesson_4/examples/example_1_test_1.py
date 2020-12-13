"""Runs my_func_1 docstring examples."""

from doctest import run_docstring_examples
from example_1_lib import my_func_1

run_docstring_examples(my_func_1, globs=globals().copy(), verbose=True,
                       name=f'{my_func_1.__name__} docstring')
