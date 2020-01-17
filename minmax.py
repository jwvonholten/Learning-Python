def minmax(test, *args):
    res = args[0]
    for x in args[1:]:
        if test(x,res): res = x
    return res

def lessthan(x,y):
    return x < y

def greaterthan(x,y):
    return x > y

print(minmax(lessthan,1,4,5))
print(minmax(greaterthan,1,4,5))
