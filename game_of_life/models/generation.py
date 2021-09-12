# -*- coding: utf-8 -*-

"""Generation entity class"""

__author__ = "vodkar"

from .cell_event import NextStateCellEvent


class Generation:
    """Generation entity class. Realize main logic of generations. Works like event storage"""

    _generation: int
    _events: list[NextStateCellEvent]

    def __init__(self) -> None:
        self._generation = 1
        self._events = []

    def next_generation(self):
        self._generation += 1

        # update states of cells
        for event in self._events:
            event.cell.has_life = event.has_life

        self._events = []

    def notify_next_state(self, next_state_event: NextStateCellEvent):
        self._events.append(next_state_event)
