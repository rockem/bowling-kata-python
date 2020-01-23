import pytest

from bowling.game import BowlingGame


@pytest.fixture()
def game():
    yield BowlingGame()


def test_gutter_game(game):
    _roll_many(game, pins=0, times=20)
    assert game.score() == 0


def _roll_many(game, pins, times):
    [game.roll(pins) for _ in range(times)]


def test_all_ones_game(game):
    _roll_many(game, pins=1, times=20)
    assert game.score() == 20
