class Score(object):
    def __init__(self, goals=0, pts=0):
        self.goals = goals
        self.pts = pts
    def __str__ (self):
        return "{} goal(s) and {} point(s)".format(self.goals, self.pts)
    def __gt__(self, other):
        return (self.goals * 3) + self.pts > (other.goals * 3) + other.pts
    def __mul__(self, n):
        z = Score()
        z.goals = self.goals * n
        z.pts = self.pts * n
        return z
    def __rmul__(self, n):
        z = Score()
        z.goals = (self.goals * n)
        z.pts = (self.pts * n)
        return z
    def __imul__(self, n):
        self.goals *= n
        self.pts *= n
        return self
