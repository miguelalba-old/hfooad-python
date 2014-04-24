"""
Gary's Game System Framework

Board classes
Author: m1ge7
Date: 2014/04/24
"""

class Tile:
    
    def __init__(self):
        self._units = []

    def add_unit(self, unit):
        self._units.append(unit)

    def remove_unit(self, unit):
        self._units.remove(unit)

    def remove_units(self):
        pass  # Not implemented in original source

    def get_units(self):
        return self._units


class Board:

    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._tiles = [[Tile()] * self._height]] * self._width

    def get_tile(self, x, y):
        return self._tiles[x-1][y-1]

    def add_unit(self, unit, x, y):
        self._tiles[x][y].add_unit(unit)
