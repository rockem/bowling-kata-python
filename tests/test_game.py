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


def test_one_spare_game(game):
    _roll_spare(game)
    game.roll(3)
    _roll_many(game, pins=0, times=17)
    assert game.score() == 16


def _roll_spare(game):
    game.roll(4)
    game.roll(6)


def test_one_strike_game(game):
    _roll_strike(game)
    game.roll(3)
    game.roll(6)
    _roll_many(game, pins=0, times=16)
    assert game.score() == 28


def _roll_strike(game):
    game.roll(10)


def test_strike_in_last_frame_game(game):
    _roll_many(game, pins=0, times=18)
    _roll_strike(game)
    game.roll(4)
    game.roll(2)
    assert game.score() == 16
