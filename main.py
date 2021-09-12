# -*- coding: utf-8 -*-

"""Entry point"""

__author__ = "vodkar"

from game_of_life.models import CycledGrid, LifeGame
from game_of_life.ui import get_drawer
from game_of_life.config import load_config
from time import sleep

if __name__ == "__main__":
    config = load_config()
    drawer = get_drawer(config.grid_drawer)
    game = LifeGame(
        CycledGrid((config.height, config.width), [(cell.height, cell.width) for cell in config.seed_cells])
    )

    while True:
        drawer.draw(game.grid)
        sleep(config.delay)
        game.next_loop()
