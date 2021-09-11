# -*- coding: utf-8 -*-

"""Exceptions"""

__author__ = "vodkar"

from enum import Enum


class PopulatingErrorTypes(Enum):
    ALREADY_POPULATED = "Cell already populated"
    ALREDY_UNPOPULATED = "Cell already unpopulated"


class PopulatingError(Exception):
    cell = ...
    error: PopulatingErrorTypes = ...

    def __init__(self, cell, error: PopulatingErrorTypes, *args: object) -> None:
        self.cell = cell
        self.error = error
        super().__init__(*args)()
