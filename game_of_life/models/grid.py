# -*- coding: utf-8 -*-
from __future__ import annotations

"""Grid of game life class file"""

__author__ = "vodkar"


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

    def iterate_over_grid(self):
        return iter((k, n) for k in range(self._size[0]) for n in range(self._size[1]))

    def __iter__(self):
        return iter(x for row in self._grid for x in row)

    def __eq__(self, o: Grid) -> bool:
        return self._size == o._size and self._grid == o._grid

    @property
    def grid(self):
        return self._grid


class CycledGrid(Grid):
    def _mod_get_cell(self, k, n):
        return self._grid[k % self._size[0]][n % self._size[1]]

    def get_neighborhoods(self, k: int, n: int) -> tuple[list[Cell], int]:
        """Get neighborhoods cells and count of live cells

        Args:
            k (int): row
            n (int): column

        Returns:
            tuple[list[Cell], int]: neighborhoods cells and count of live cells
        """
        up, down, left, right = k - 1, k + 1, n - 1, n + 1
        neighs = [
            self._mod_get_cell(up, left),
            self._mod_get_cell(up, n),
            self._mod_get_cell(up, right),
            self._mod_get_cell(k, left),
            self._mod_get_cell(k, right),
            self._mod_get_cell(down, left),
            self._mod_get_cell(down, n),
            self._mod_get_cell(down, right),
        ]
        return neighs, sum(cell.has_life for cell in neighs)