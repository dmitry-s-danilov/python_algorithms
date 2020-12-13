from problem_1_func import func_2

s = 'abracadabra'

print(f'string: {s}',
      f'substrings number: {func_2(s)}',
      'substring frequencies:',
      sep='\n')

for _ in sorted(func_2(s, verbose=True).items(),
                key=lambda _: _[1],
                reverse=True):
    print(*_, sep=': ')
