class Weight(object):
    OUNCES_PER_POUND = 16
    def __init__(self, pounds=0, ounces=0):
        self.pounds = pounds
        self.ounces = ounces

    def to_ounces(self):
        ounces = self.ounces
        ounces += self.pounds * self.OUNCES_PER_POUND
        return ounces

    def __eq__(self, other):
        return self.to_ounces() == other.to_ounces()

    def __gt__(self, other):
        return self.to_ounces() > other.to_ounces()

    def __ge__(self, other):
        return self.to_ounces() >= other.to_ounces()

    def __add__(self, other):
        return Weight.from_ounces(self.to_ounces() + other.to_ounces())

    def __iadd__(self, other):
        z = self + other
        self.pounds = z.pounds
        self.ounces = z.ounces
        return z

    def __mul__(self, n):
        return Weight.from_ounces(self.to_ounces() * n)

    def __imul__(self, n):
        z = Weight.from_ounces(self.to_ounces() * n)
        self.pounds = z.pounds
        self.ounces = z.ounces
        return z

    def __rmul__(self, n):
        return Weight.from_ounces(self.to_ounces() * n)

    def __sub__(self, other):
        return Weight.from_ounces(self.to_ounces() - other.to_ounces())

    def __isub__(self, other):
        z = self - other
        self.pounds = z.pounds
        self.ounces = z.ounces
        return z

    def __str__(self):
        return "{} pound(s) and {} ounce(s)".format(self.pounds, self.ounces)

    @classmethod
    def from_ounces(cls, ounces):
        pounds, ounces = divmod(ounces, cls.OUNCES_PER_POUND)
        return cls(pounds, ounces)
