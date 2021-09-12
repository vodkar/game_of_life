# -*- coding: utf-8 -*-

"""Interface to draw grid file"""

__author__ = "vodkar"

from abc import ABC, abstractmethod
import os

from ..models import Grid


class IGridDrawer(ABC):
    def draw(self, grid: Grid):
        """Method to draw grid

        Args:
            grid (Grid): gtid to deaw
        """


class ConsoleGridDrawer(IGridDrawer):
    def __init__(self, live_cell="■", dead_cell="□") -> None:
        self._live_cell = live_cell
        self._dead_cell = dead_cell
        super().__init__()

    def draw(self, grid: Grid):
        os.system("cls")
        for row in grid.grid:
            for cell in row:
                if cell.has_life:
                    print(self._live_cell)
                else:
                    print(self._dead_cell)
            print("\n")