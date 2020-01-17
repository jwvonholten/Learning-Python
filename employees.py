# file employees.py

class Employee:
    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary
    def giveRaise(self,percent):
        self.salary = self.salary + (self.salary * percent)
    def work(self):
        print(self.name, 'does stuff')
    def __repr__(self):
        return '<Employee: name=%s, salary=%s>' % (self.name, self.salary)

class Chef(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 50000)
    def work(self):
        print(self.name, 'makes food')

class Server(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 40000)
    def work(self):
        print(self.name, 'interfaces with customers')

class PizzaRobot(Chef):
    def __init__(self, name):
        Chef.__init__(self, name)
    def work(self):
        print(self.name, 'makes pizza')

if __name__ == '__main__':
    bob = PizzaRobot('bob')     #make robot bob
    print(bob)                  #run inherited method __str__
    bob.work()                  #run type specific action
    bob.giveRaise(.20)
    print(bob)
    print()

    for k in [Employee, Chef, Server, PizzaRobot]:
        obj = k(k.__name__)
        obj.work()

    
