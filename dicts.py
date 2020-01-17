
def copyDict(old):
    new =dict()
    for x in old.keys():
        new[x] = old[x]
    return new
    
def addDict(dict1, dict2):
    new = dict()
    for x in dict1.keys():
        new[x] = dict1[x]
    for x in dict2.keys():
        new[x] = dict2[x]
    return new

d1 = {'a':1,'b':2,'c':3}
d2 = {'a':1,'b':2,'d':4,'e':6}

print(copyDict(d1))

print(addDict(d1,d2))

input('press enter to continue')
