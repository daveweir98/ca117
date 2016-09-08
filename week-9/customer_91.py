class Customer(object):
    disc = 0
    def __init__(self, name, balance, addr1, addr2, addr3):
        self.name = name
        self.balance = balance
        self.addr1 = addr1
        self.addr2 = addr2
        self.addr3 = addr3

    def owes(self):
        return self.balance - (self.balance * (self.disc/100))
    def __str__(self):
        return "{}\n{}\n{}\n{}\nBalance: {:.2f}\nDiscount: {}%\nAmount due: {:.2f}".format(self.name, self.addr1, self.addr2, self.addr3, float(self.balance), self.disc, float(self.owes()))

class ValuedCustomer(Customer):
    disc = 10
