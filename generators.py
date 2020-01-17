def gensquares(N):
    for i in range(N):
        yield i ** 2

x = gensquares(4)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))


def gen():
    for i in range(10):
        x = yield i
        print(x)

G = gen()
next(G)
G.send(77)
G.send(88)
next(G)

def ups(line):
    for sub in line.split(','):
        yield sub.upper()

print(tuple(ups('aaa,bbb,ccc')))

print({i:s for (i,s) in enumerate(ups('aaa,bbb,ccc'))})