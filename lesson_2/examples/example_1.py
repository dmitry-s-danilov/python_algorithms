"""
Example 1
Print digits of integer number (pre-conditioned loop)
"""

num = int(input('input integer number: '))
while num:
    print(num % 10)
    num //= 10
