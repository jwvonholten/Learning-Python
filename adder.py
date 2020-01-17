
def adder(x,y):
    return x + y

def adderv(*pargs):
    res = pargs[0]
    for x in pargs[1:]:
        res = res + x
    return res

def adderd(good=1,bad=2,ugly=3):
    return good + bad + ugly

def copyDict(**d):
    return dict(d)
    
#def addDict(dict1, dict2):
    
z = adder(12,15)
print(z)

z = adder('sp','am')
print(z)

z = adder([1,2],[3])
print(z)

z = adderv(12,15)
print(z)

z = adderv('sp','am')
print(z)

z = adderv([1,2],[3])
print(z)

#z = adderv({'a':1},{'b':2})
#print(z)

d = {'a':1,'b':2,'c':3}
print(copyDict(**d))


input('press enter to continue')
