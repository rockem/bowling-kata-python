class BowlingGame:
    _score = 0

    def __init__(self):
        self._rolls = []

    def roll(self, pins):
        self._rolls.append(pins)

    def score(self):
        return sum([roll for roll in self._rolls])
