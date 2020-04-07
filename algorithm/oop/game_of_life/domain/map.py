# -*- coding: utf-8 -*-
class Map:
    def __init__(self, x, y):
        self.map = [[None for i in range(x)] for j in range(y)]
        self.x = x
        self.y = y

    def get_map(self):
        return self.map

    def set_cell(self, x=None, y=None, cell=None):
        if x is None or y is None or cell is None:
            raise AssertionError
        self.map[y][x] = cell

    def get_cell(self, x=None, y=None):
        if -1 >= x or x >= self.x or -1 >= y or y >= self.y:
            raise AssertionError

        return self.map[y][x]

    def pprint(self):
        for i in self.map:
            print([cell.get_status() for cell in i])
