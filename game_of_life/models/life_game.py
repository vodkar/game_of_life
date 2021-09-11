# -*- coding: utf-8 -*-

"""Life game entity"""

__author__ = "vodkar"

from .cell_event import CellWillDieEvent, CellWillLiveEvent
from .generation import Generation
from .grid import Grid


class LifeGame:
    def __init__(self, grid: Grid) -> None:
        self._grid = grid
        self._generation = Generation()

    def next_loop(self):
        for k, n in self._grid.iterate_over_grid():
            cell = self._grid.get_cell(k, n)
            lifes_count = sum(cell.has_life for cell in self._grid.get_neighborhoods(k, n))

            if lifes_count >= 2 and lifes_count <= 3:
                event = CellWillLiveEvent(cell)
            else:
                event = CellWillDieEvent(cell)

            self._generation.notify_next_state(event)

        self._generation.next_generation()
