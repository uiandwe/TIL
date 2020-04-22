# -*- coding: utf-8 -*-
import threading
import time


def ourThread(i):
    print("thread {} start".format(i))
    time.sleep(i*2)
    print("thread {} finish".format(i))


if __name__ == '__main__':
    thread1 = threading.Thread(target=ourThread, args={1, })
    thread1.start()
    print("is thread 1 finished???")
    thread2 = threading.Thread(target=ourThread, args={2, })
    thread2.start()
    thread2.join()
    print("thread 2 finished")

"""
thread 1 start
thread 1 finish
is thread 1 finished???
thread 2 start
thread 2 finish
thread 2 finished
"""
