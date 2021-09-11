# -*- coding: utf-8 -*-

"""Grid of game life class file"""

__author__ = "vodkar"

from __future__ import annotations

from abc import ABC, abstractmethod
from inject import params

from .cell import Cell


# In case if we want cycled or not cycled grid
class Grid(ABC):
    _grid: list[list[Cell]] = ...

    def __init__(
        self,
        size: tuple[int, int],
        live_cells: set[tuple[int, int]],
    ) -> None:
        self._grid = []
        self._size = size

        for i in range(size[0]):
            row = []
            for j in range(size[1]):
                # check if this cell should has life
                has_life = (i, j) in live_cells
                row.append(Cell(has_life))

            self._grid.append(row)

    def get_cell(self, k, n) -> Cell:
        return self._grid[k][n]

    @abstractmethod
    def get_neighborhoods(self, k, n) -> list[Cell]:
        """Return neighorhoods from grid

        Args:
            grid (Grid): life grid
            k (int): row index
            n (int): column index

        Returns:
            list[Cell]: [description]
        """


class CycledGrid(Grid):
    def _mod_get_cell(self, k, n):
        return self._grid[k % self._size[0], n % self._size[1]]

    def get_neighborhoods(self, k, n) -> list[Cell]:
        up, down, left, right = k - 1, k + 1, n - 1, n + 1
        return [
            self._mod_get_cell(up, left),
            self._mod_get_cell(up, n),
            self._mod_get_cell(up, right),
            self._mod_get_cell(k, left),
            self._mod_get_cell(k, n),
            self._mod_get_cell(k, right),
            self._mod_get_cell(down, left),
            self._mod_get_cell(down, n),
            self._mod_get_cell(down, right),
        ]