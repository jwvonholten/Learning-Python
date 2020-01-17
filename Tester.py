from scramble import scramble
from inter2 import intersect, union
from permute import permute1, permute2

def tester(func, items, trace=True):
    for args in scramble(items):
        if trace: print(args)
        print(sorted(func(*items)))


#tester(intersect,('abb','abcdefg','abdst','albmcmd'))

#tester(union,('a','abcdefg','abdst','albmcmd'), False)

print(permute1('abc'))
#G = permute2('abc')
#print(next(G))