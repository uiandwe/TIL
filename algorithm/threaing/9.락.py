# -*- coding: utf-8 -*-
import threading
import time
import random

lock = threading.Lock()

count = 0

def workerA():
    global count
    lock.acquire()
    try:
        while count < 10:
            count += 1
            print("worker A {}".format(count))
            time.sleep(random.randint(0, 1))
    finally:
        lock.release()


def workerB():
    global count
    lock.acquire()
    try:
        while count > 0:
            count -= 1
            print("worker B {}".format(count))
            time.sleep(random.randint(0, 1))
    finally:
        lock.release()

if __name__ == '__main__':
    thread1 = threading.Thread(target=workerA)
    thread2 = threading.Thread(target=workerB)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    print("thread 2 finished")

