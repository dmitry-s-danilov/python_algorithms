from problem_8_lib import my_print

# set a list of matrices
t = ([[]], [[1]], [[1, 2]],
     [[], []], [[1], [2]], [[1, 2], [3, 4]], [[1, 2, 3], [4, 5, 6]])

# apply function to all matrices from the list
for z in t:
    print(f'size: {len(z)} x {len(z[0])}',
          f'print: {z}',
          'my_print:',
          sep='\n')
    my_print(z)
