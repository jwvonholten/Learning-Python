
def min1(*pargs):
    ret = pargs[0]
    for x in pargs[1:]:
        if x < ret:
            ret = x
    return ret

def min2(f ,*pargs):
    ret = f
    for x in pargs:
        if x < ret:
            ret = x
    return ret

def min3(*pargs):
    L = sorted(list(pargs))
    return L[0]

print(min1(4,5,6))
print(min1('A','B','C'))
print(min1('spam','eggs','ham'))

print(min2(4,5,6))
print(min2('A','B','C'))
print(min2('spam','eggs','ham'))

print(min3(4,5,6))
print(min3('A','B','C'))
print(min3('spam','eggs','ham'))
