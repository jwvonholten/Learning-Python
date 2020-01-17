# permute.py

def permute1(seq):
    #normal recursive function
    if not seq: return [seq]    #empty seq
    else:
        res = []
        for i in range(len(seq)):
            rest = seq[:i] + seq[i+1:]  #delete current node
            #print(i, rest)
            for x in permute1(rest):    # permute the others
                res.append(seq[i:i+1]+x)    #add node at front
        return res

def permute2(seq):
    #recursive generator
    if not seq: yield seq       #empty seq
    else:
        for i in range(len(seq)):
            rest = seq[:i] + seq[i+1:]  #delete current node
            for x in permute2(rest):    #permute the others
                yield seq[i:i+1] + x    #add node at front
