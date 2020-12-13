from problem_1_func import func_1

s = 'abracadabra'

print(f'string: {s}',
      f'substrings number: {func_1(s)}',
      'substrings sequence:',
      sep='\n')

for _ in enumerate(sorted(func_1(s, verbose=True),
                          key=lambda _: len(_)),
                   1):
    print(*_)
