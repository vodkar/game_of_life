# -*- coding: utf-8 -*-

"""Life cell entity file"""

__author__ = "vodkar"


class Cell:
    _has_life: bool

    def __init__(self, has_life: bool) -> None:
        self._has_life = has_life

    @property
    def has_life(self) -> bool:
        """Is there life in this cell

        Returns:
            bool: True if exists else False
        """
        return self._has_life

    @has_life.setter
    def has_life(self, value: bool):
        self._has_life = value

    # def unpopulated(self):
    #     if self._has_life:
    #         CellWillDieEvent(self)
    #     else:
    #         raise PopulatingError(self, PopulatingErrorTypes.ALREDY_UNPOPULATED)

    # def populated(self):
    #     if not self._has_life:
    #         CellWillLiveEvent(self)
    #     else:
    #         raise PopulatingError(self, PopulatingErrorTypes.ALREADY_POPULATED)
