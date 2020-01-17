# file person.py
"""
Record and process information about people.
Run this file directly to test its classes
"""

from classtools import AttrDisplay


class Person(AttrDisplay):
    """
    Create and process person records
    """
    def __init__(self, name, job=None, pay=0): #Constructor takes these args
        self.name = name                # fill out each attribute when created
        self.job = job                  # self is the new instance object
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

class Manager(Person):
    """
    Customized Person with special requirments
    """
    def __int__(self,name,pay):
        Person.__init__(self,name,'Mgr',pay)
    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)
                       
if __name__ == '__main__':
    # self test code
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='Developer', pay=100000)
    print(bob.lastName())
    print(sue.lastName())
    print(bob)
    print(sue)
    sue.giveRaise(.10)
    print(sue)
    tom = Manager('Tom Jones',pay=50000)
    print(tom)
    tom.giveRaise(.10,.5)
    print(tom)
    print('--- all 3 ---')
    for x in (bob, sue, tom):
        print(x)
        x.giveRaise(.10)
        print(x)
