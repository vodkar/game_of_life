from copy import deepcopy
import unittest
from game_of_life import __version__
from game_of_life.models import LifeGame, CycledGrid


def test_version():
    assert __version__ == "0.1.0"


def test_pattern(steps: list[CycledGrid]):
    game = LifeGame(steps[0])
    for step in steps[1:]:
        game.next_loop()
        yield step == game.grid


class TestBlockPatternLife(unittest.TestCase):
    def test_block_pattern(self):
        block_grid = CycledGrid((4, 4), {(1, 1), (1, 2), (2, 1), (2, 2)})

        assert all(test_pattern([block_grid, deepcopy(block_grid), deepcopy(block_grid)]))


if __name__ == "__main__":
    unittest.main()