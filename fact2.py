
def f0(n):
    if n == 1: return 1
    return f0(n - 1) * n

from functools import reduce
def f1(n):
    return reduce((lambda x, y: x * y), range(1,n + 1))

print(6, f0(6))
print(6, f1(6))
print(5, f1(5))
