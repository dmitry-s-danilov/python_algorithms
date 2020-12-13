"""
Example 5
Convert from bytes to kilobytes or vice versa.
"""

num = int(input('input integer number: '))

ans = input("convert to bytes - 'b', kilobytes - 'k': ")
ans = ans.lower()

if ans == 'b':
    print(f'bytes: {num * 1024}')
elif ans == 'k':
    print(f'bytes: {num / 1024}')
else:
    print('invalid input')
