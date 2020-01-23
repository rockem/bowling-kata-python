NUMBER_OF_FRAMES = 10


class BowlingGame:
    def __init__(self):
        self._rolls = []

    def roll(self, pins):
        self._rolls.append(pins)

    def score(self):
        score = 0
        first_in_frame = 0
        for i in range(NUMBER_OF_FRAMES):
            if self._is_strike(first_in_frame):
                score += 10 + self._rolls[first_in_frame + 1] + self._rolls[first_in_frame + 2]
                first_in_frame += 1
            elif self._is_spare(first_in_frame):
                score += 10 + self._rolls[first_in_frame + 2]
                first_in_frame += 2
            else:
                score += self._rolls[first_in_frame] + self._rolls[first_in_frame + 1]
                first_in_frame += 2
        return score

    def _is_strike(self, first_in_frame):
        return self._rolls[first_in_frame] == 10

    def _is_spare(self, first_in_frame):
        return self._rolls[first_in_frame] + self._rolls[first_in_frame + 1] == 10
