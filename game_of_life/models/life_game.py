# -*- coding: utf-8 -*-

"""Life game entity"""

__author__ = "vodkar"

from .generation import Generation
from .grid import Grid


class LifeGame:
    def __init__(self, grid: Grid) -> None:
        self._grid = grid
        self._generation = Generation()

    def next_loop(self):
        self._generation.next_generation()
