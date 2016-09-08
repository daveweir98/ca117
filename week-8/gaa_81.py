
class Score(object):
    def __init__(self, goals=0, pts=0):
        self.goals = goals
        self.pts = pts

    def __str__(self):
        return "{} goal(s) and {} point(s)".format(self.goals, self.pts)

    def __eq__(self, other):
        return (self.goals * 3) + self.pts == (other.goals * 3) + other.pts

    def __gt__(self, other):
        return (self.goals * 3) + self.pts > (other.goals * 3) + other.pts

    def __ge__(self, other):
        return (self.goals * 3) + self.pts >= (other.goals * 3) + other.pts

    def __add__(self, other):
        z = Score()
        z.goals = self.goals + other.goals
        z.pts = self.pts + other.pts
        return z

    def __sub__(self, other):
        z = Score()
        z.goals = self.goals - other.goals
        z.pts = self.pts - other.pts
        return z

    def __iadd__(self, other):
        self.goals += other.goals
        self.pts += other.pts
        return self

    def __isub__(self, other):
        self.goals -= other.goals
        self.pts -= other.pts
        return self
