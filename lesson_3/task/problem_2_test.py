import doctest
from problem_2_lib import my_func

doctest.run_docstring_examples(my_func, globals().copy(), verbose=True,
                               name=f'{my_func.__name__} docstring')
