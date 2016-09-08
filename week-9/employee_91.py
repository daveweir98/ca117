class Employee(object):
    def __init__ (self, name, num):
        self.name = name
        self.num = num
    def wages(self):
        return 0
    def __str__(self):
        return "Name: {}\nNumber: {}\nWages: {:.2f}".format(self.name, self.num, self.wages())

class Manager(Employee):
    def __init__(self, name, num, salary):
        self.name = name
        self.num = num
        self.salary = salary
    def wages(self):
        return self.salary / 52

class AssemblyWorker(Employee):
    def __init__(self, name, num, rate, hours):
        self.name = name
        self.num = num
        self.rate = rate
        self.hours = hours
    def wages(self):
        return self.rate * self.hours
