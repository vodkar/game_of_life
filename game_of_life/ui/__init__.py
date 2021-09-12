# -*- coding: utf-8 -*-
# flake8: noqa
from .grid_drawer import IGridDrawer, ConsoleGridDrawer

_configs = {"console": ConsoleGridDrawer}


def get_drawer(config: str) -> IGridDrawer:
    return _configs[config]()