"""
Highest common denom
"""

def comDenom(*P):
    for x in range(min(P),0,-1):
        if all(y % x == 0 for y in P):
            return x

def comDenom2(*P):
    for x in range(min(P),0,-1):
        for y in P:
            if y % x != 0:
                break
        else:
            return x

print(comDenom(12,144))
print(comDenom(12,144,512))
print(comDenom(12,144,512,2))
print(comDenom(12,144,100))
print(comDenom(12,144,5))

print(comDenom2(12,144))
print(comDenom2(12,144,512))
print(comDenom2(12,144,512,2))
print(comDenom2(12,144,100))
print(comDenom2(12,144,5))

print(comDenom(100000000,123456789))
