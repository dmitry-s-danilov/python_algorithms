"""Runs docstring examples of specified function."""

from doctest import run_docstring_examples
from example_2_lib_fib import fib_1

func = fib_1
run_docstring_examples(func, globs=None, verbose=True,
                       name=f'{func.__name__} docstring')
