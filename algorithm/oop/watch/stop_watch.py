# -*- coding: utf-8 -*-
import time
from .time_ import Time_


class StopWatch:

    def __init__(self):
        self._start_time = 0
        self._stop_time = 0

    def start(self):
        self._start_time = time.time()

    def end(self):
        self._stop_time = time.time()

    def get_elapsed_time(self):
        return Time_(self._stop_time - self._start_time)
