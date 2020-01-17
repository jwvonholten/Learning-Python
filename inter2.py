def intersect(*args):
    res = []
    for x in args[0]:               #scan first seq
        if x in res: continue       #skip duplicates
        for y in args[1:]:              #for all other args
            if x not in y: break    #Item in each one?
        else:
            res.append(x)
    return res

def union(*args):
    res = []
    for x in args:
        for y in x:
            if y not in res:
                res.append(y)
    return res


            
            
