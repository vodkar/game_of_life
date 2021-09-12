# -*- coding: utf-8 -*-

"""Configuration file"""

__author__ = "vodkar"

from dataclasses import dataclass
from enum import Enum

from yaml import load, SafeLoader


CONFIG_FILE = "config.yaml"
SEED_CELLS = "seed_cells"
HEIGHT_FIELD = "height"
WIDTH_FIELD = "width"
DRAWER_FIELD = "drawer"
DELAY_FIELD = "delay"


@dataclass(frozen=True)
class CellConfig:
    height: int
    width: int


@dataclass(frozen=True)
class LifeConfig:
    height: int
    width: int
    grid_drawer: str
    delay: float
    seed_cells: list[CellConfig]


def load_config() -> LifeConfig:
    """
    Load config from CONFIG_FILE
    """
    config = load(open(CONFIG_FILE, "r+", encoding="utf-8"), SafeLoader)["LifeConfig"]
    cells = [CellConfig(cell[HEIGHT_FIELD], cell[WIDTH_FIELD]) for cell in config.get(SEED_CELLS, [])]
    return LifeConfig(
        config[HEIGHT_FIELD], config[WIDTH_FIELD], config[DRAWER_FIELD], config[DELAY_FIELD], cells
    )
