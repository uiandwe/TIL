# -*- coding: utf-8 -*-
"""
populated 되어있는 공간에서는

    이웃이 하나 이하라면 외로움에 죽는다.

    이웃이 4개 이상이면 갑갑해서 죽는다.

    이웃이 2개나 3개이면 살아남는다.

빈공간이나 unpopulated 되어있는 공간에서는

    이웃이 3 개이면 populated 된다 (증식된다).
"""

import time
from oop.game_of_life.controller.map_controller import MapController


if __name__ == '__main__':

    d = [[0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0],
         [0, 0, 0, 1, 0],
         [0, 1, 1, 1, 0],
         [0, 0, 0, 0, 0]]

    mp = MapController()
    mp.init_map(d)

    # mp.pp()
    # mp.cell_update()
    # mp.pp()

    step = 0
    while step < 10:
        step += 1
        mp.cell_update()
        mp.pp()
        time.sleep(1)

