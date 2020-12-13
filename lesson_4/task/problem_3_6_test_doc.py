from doctest import run_docstring_examples
from problem_3_6_lib import my_func_1

# set an object containing examples
func = my_func_1
# set a name for using in messages
func_name = func.__name__
# test examples associated with object
run_docstring_examples(func, name=func_name,
                       globs=globals(), verbose=True)
