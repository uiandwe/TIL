# -*- coding: utf-8 -*-
import copy
from oop.game_of_life.domain.map import Map
from oop.game_of_life.domain.cell import Cell
from oop.game_of_life.domain.status import Status

from oop.game_of_life.controller.cell_controller import CellController


class MapController:
    def __init__(self):
        self.map = None
        self.width = None
        self.height = None

    def init_map(self, map):
        self.height = len(map)
        self.width = len(map[0])

        self.map = Map(self.width, self.height)

        for i in range(self.height):
            for j in range(self.width):
                cell_init_status = map[i][j]
                status = Status(cell_init_status)
                cell = Cell(status)
                self.map.set_cell(j, i, cell)

    def cell_update(self):
        cc = CellController(self.width, self.height)
        self.map = cc.update(self.map)

    def pp(self):
        print("==========")
        self.map.pprint()
