# -*- coding: utf-8 -*-

"""Life game entity"""

__author__ = "vodkar"

from .cell import Cell
from .cell_event import CellWillDieEvent, CellWillLiveEvent
from .generation import Generation
from .grid import Grid


class LifeGame:
    def __init__(self, grid: Grid) -> None:
        self._grid = grid
        self._generation = Generation()

    def is_underpopulation_or_overpopulation(self, cell: Cell, lifes_count: int) -> bool:
        """Check if cell will underpopulated or overpopulated

        Args:
            cell (Cell): cell to check
            lifes_count (int): count of lifes in nieghborhoods

        Returns:
            bool: -
        """
        return cell.has_life and (lifes_count < 2 or lifes_count > 3)

    def is_reproduction(self, cell: Cell, lifes_count: int) -> bool:
        """Check if cell will reproducted

        Args:
            cell (Cell): cell to check
            lifes_count (int): count of lifes in neighorhoods

        Returns:
            bool: is reproducted
        """
        return not cell.has_life and lifes_count == 3

    def next_loop(self):
        for k, n in self._grid.iterate_over_grid():
            current_cell = self._grid.get_cell(k, n)
            _, lifes_count = self._grid.get_neighborhoods(k, n)

            event = None
            if self.is_reproduction(current_cell, lifes_count):
                event = CellWillLiveEvent(current_cell)
            elif self.is_underpopulation_or_overpopulation(current_cell, lifes_count):
                event = CellWillDieEvent(current_cell)

            if event:
                self._generation.notify_next_state(event)

        self._generation.next_generation()

    @property
    def grid(self):
        return self._grid