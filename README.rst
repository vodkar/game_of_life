===========
Game "Life"
===========
--------
Settings
--------
Settings provided by ``config.yaml`` file. You can copy ``config.copy.yaml`` and fill that file as you want.

- ``height``: height of life grid
- ``width``: width of life grid
- ``seed_cells``: initialization cells have height and width also. indexing from 0.
- ``drawer``: how to draw grid. Only "console" is available for now
- ``delay``: delay between generations

--------
Launch
--------
~~~~~~~~~~
Poetry
~~~~~~~~~~
Using poetry, install packages: ``poetry install``

~~~~~~~~~~
Docker
~~~~~~~~~~
| Using docker: 
| ``docker build -t game_life .`` 
| I hope it's work for you
