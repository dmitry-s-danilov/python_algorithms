"""
Example 8
Find all primes smaller than a given integer number.
"""

n = int(input('input integer number: '))
# x = list(range(n))
x = [i for i in range(n)]
x[1] = 0
for i in range(2, n):
    if x[i] != 0:
        j = i * 2
        while j < n:
            x[j] = 0
            j += i
# y = []
# for i in x:
#     if i != 0:
#         y.append(i)
y = [i for i in x if i]
print(y)
