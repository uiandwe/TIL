# -*- coding: utf-8 -*-
import copy
from oop.game_of_life.domain.status import Status


class CellController:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_neighbor_cell_count(self, x, y, map):
        dx = [-1, 0, 1, -1, 1, -1, 0, 1]
        dy = [-1, -1, -1, 0, 0, 1, 1, 1]

        neighbor_cell_count = 0
        for next_index in range(len(dx)):
            next_x = dx[next_index] + x
            next_y = dy[next_index] + y
            if 0 <= next_x < self.width and 0 <= next_y < self.height:
                if map.get_cell(next_x, next_y).get_status() != Status.die:
                    neighbor_cell_count += 1

        return neighbor_cell_count

    def update(self, map):
        copy_map = copy.deepcopy(map)
        for i in range(self.height):
            for j in range(self.width):
                count = self.get_neighbor_cell_count(j, i, map)
                copy_map.get_cell(j, i).update_status(count)
        return copy_map
