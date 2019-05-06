# -*- coding: utf-8 -*-
import collections
from threading import Lock, Thread

class MyQueue(object):
    def __init__(self):
        self.items = collections.deque()
        self.lock = Lock()

    def put(self, item):
        with self.lock:
            self.items.append(item)

    def get(self):
        with self.lock:
            return self.items.popleft()

import time

class Worker(Thread):
    def __init__(self, func, in_queue, out_queue):
        super().__init__()
        self.func = func
        self.in_queue = in_queue
        self.out_queue = out_queue

        self.polled_count = 0
        self.work_done = 0


    def run(self):
        while True:
            self.polled_count += 1
            try:
                item = self.in_queue.get()
            except IndexError:
                time.sleep(0.01)
            else:
                result = self.func(item)
                self.out_queue.put(result)
                self.work_done += 1


from queue import Queue
queue = Queue()

def consumer():
    print('consumer wating')
    queue.get()
    print('done')

thread = Thread(target=consumer)
thread.start()

# queueu.put() 하지 않으면 위에서 멈춤
print('producer ')
queue.put(object())
thread.join()
print('done')


print('===============================')
# queue 갯수를 1로 조정하여 다음번을 대기 상태로 둘수 있음
queue = Queue(1)

def consumer1():
    time.sleep(0.1)
    queue.get()
    print('got 1')
    queue.get()
    print('got 2')

thread = Thread(target=consumer1)
thread.start()

queue.put(object())
print('put 1')
queue.put(object())
print('put 2')
thread.join()
print('done')
