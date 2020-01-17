S = 'spam'

for x in S:
    print(ord(x))

SSum = 0
for x in S:
    SSum += ord(x)

print(SSum)

L = []
for x in S:
    L.append(ord(x))

print(L)

print(list(map(ord,S)))

print([ord(c) for c in S])

D = {'a':1,'b':2,'c':3,'d':4}

print(D)

for x in sorted(D.keys()):
    print (x , D[x])

L = [1,2,4,8,16,32,64]

X = 5

found = False

i = 0

while not found and i < len(L):
    if 2 ** X == L[i]:
        found = True
    else:
        i = i+1

if found:
    print('at index' , i) #1
else:
    print('not found')



i = 0

while i < len(L):
    if 2 ** X == L[i]:
        print('at index' , i) #2
        break
    else:
        i = i+1
else:
    print('not found')


for N in L:
    if 2 ** X == N:
        print('at index' , L.index(N)) #3
        break
else:
    print('not found')

if 2 ** X in L:
    print('at index' , L.index(2 ** X)) #4
else:
    print('not found')

L = []
for I in range(7):
    L.append(2 ** I)
print(L)

L = [ 2 ** I for I in range(7)]
print(L)

L = list(map(lambda x: 2 ** x, range(7)))
print(L)




        
