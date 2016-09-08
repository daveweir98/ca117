import random

class Coin(object):
    def __init__(self, sideup="Heads"):
        self.sideup = sideup

    def flip(self):
        self.sideup = random.choice(["Heads", "Tails"])

    def getstate(self):
        return self.sideup

    def __str__(self):
        return "Current state : {}".format(self.sideup)
