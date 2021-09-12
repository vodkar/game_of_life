# -*- coding: utf-8 -*-

"""Events in game"""

__author__ = "vodkar"

from abc import ABC, abstractproperty
from .cell import Cell


class NextStateCellEvent(ABC):
    cell: Cell

    def __init__(self, cell: Cell) -> None:
        self.cell = cell
        super().__init__()

    @abstractproperty
    def has_life(self) -> bool:
        """State of cell in next generation

        Returns:
            bool: True or false
        """
        pass


class CellWillLiveEvent(NextStateCellEvent):
    @property
    def has_life(self) -> bool:
        return True


class CellWillDieEvent(NextStateCellEvent):
    @property
    def has_life(self):
        return False