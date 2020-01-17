# makedb.py

from person import Person, Manager
bob = Person('Bob Smith')
sue = Person('Sue Jones', job='dev', pay=100000)
tom = Manager('Tom Jones',pay=50000)

import shelve
db = shelve.open('persondb')    #file name where object are stored
for x in (bob, sue, tom):
    db[x.name] = x
db.close()
