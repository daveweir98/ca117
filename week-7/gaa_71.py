class Score(object):
    def __init__(self, goals=0, points=0):
        self.goals = goals
        self.points = points

    def greater_than(self, score):
        total1 = (self.goals * 3) + self.points
        total2 = (score.goals * 3) + score.points
        if total1 > total2:
            return True
        else:
            return False

    def equal_to(self, score):
        total1 = (self.goals * 3) + self.points
        total2 = (score.goals * 3) + score.points
        if total1 == total2:
            return True
        else:
            return False

    def less_than(self, score):
        total1 = (self.goals * 3) + self.points
        total2 = (score.goals * 3) + score.points
        if total1 < total2:
            return True
        else:
            return False
