# -*- coding: utf-8 -*-

import random


class Engine:
    min_engine_output = 1
    max_engine_output = 9
    min_move_straight = 4

    def __init__(self):
        self.engine = 0

    def run(self):
        next_distinct = self.engine_output()
        if self.min_move_straight >= next_distinct:
            self.engine += next_distinct
            return self.engine
        else:
            return 0

    def engine_output(self):
        return random.randint(self.min_engine_output, self.max_engine_output)
