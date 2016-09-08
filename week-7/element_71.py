

class Element(object):
    def __init__(self, number, name, symbol, boil):
        self.number = number
        self.name = name
        self.symbol = symbol
        self.boil = boil

    def print_details(self):
        print("Number: {}".format(self.number))
        print("Name: {}".format(self.name))
        print("Symbol: {}".format(self.symbol))
        print("Boiling Point: {} C".format(self.boil))
