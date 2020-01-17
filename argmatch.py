
def f1(a, b): print(a, b) #normal args

def f2(a, *b): print(a, b) #positional vargs

def f3(a, **b): print(a, b) #keyword kargs

def f4(a, *b, **c): print(a, b, c) # positional and keyword

def f5(a, b=2, c=3): print(a, b, c) #defaults

def f6(a, b=2, *c): print(a, b, c) #defaults and positional

