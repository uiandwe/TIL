# -*- coding: utf-8 -*-
from oop.watch.stop_watch import StopWatch
import time

if __name__ == '__main__':
    stop_watch = StopWatch()
    stop_watch.start()
    time.sleep(1)
    stop_watch.end()

    time = stop_watch.get_elapsed_time()

    print(time.get_milli_time())
    print(time.get_nano_time())
    print(time.get_second_time())
