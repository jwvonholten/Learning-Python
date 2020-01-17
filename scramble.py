# file scramble.py

def scramble(seq):
    for i in range(len(seq)):
        yield seq[i:] + seq[:i]
