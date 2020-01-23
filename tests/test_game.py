from bowling.game import BowlingGame


def test_gutter_game():
    game = BowlingGame()
    [game.roll(0) for _ in range(20)]
    assert game.score() == 0


def test_all_ones_game():
    game = BowlingGame()
    [game.roll(1) for _ in range(20)]
    assert game.score() == 20
