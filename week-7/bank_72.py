class BankAccount(object):
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            return self.balance
        else:
            print("Insufficient funds available")

    def __str__(self):
        return "Your current balance is: {}.00 euro".format(self.balance)
