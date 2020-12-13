from problem_8_lib import my_func, my_print

q = 'q'
c = f"Input two integers to set a size of matrix or '{q}' to quit: "
while True:
    s = input(c).strip()
    if s == q:
        break
    else:
        m, n = [int(_) for _ in s.split()]
        print('Fill:')
        z = my_func(m, n)
        print('Returns:')
        my_print(z)
