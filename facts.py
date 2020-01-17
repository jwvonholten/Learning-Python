
from functools import reduce
import math
from timeit import repeat

def fact1(n):
    if n == 1: return n
    else:
        return (fact1(n -1) * n)

def fact2(n):
    return reduce((lambda x, y: x * y),range(1,n +1))

def fact3(n):
    ret = 1
    for x in range(1,n+1):
        ret = ret * x
    return ret

def fact4(n):
    return math.factorial(n)

print(fact1(6))
print(fact2(6))
print(fact3(6))
print(fact4(6))

for test in (fact1, fact2, fact3, fact4):
    print(test.__name__,min(repeat(stmt=lambda: test(500), number=20, repeat=3)))
    
print(min(repeat(number=10000,repeat=3,stmt=lambda: fact1(500))))


    
