# -*- coding: utf-8 -*-
import threading


def add(res, num):
    print("start add func")
    for i in range(num):
        res += i
    print("end add func")


thread = threading.Thread(target=add, args=(0, 100))
thread.start()

class Add(threading.Thread):
    def __init__(self, value, end):
        self.value = value
        self.end = end
        threading.Thread.__init__(self)

    def start(self):
        print("start add class")
        for i in range(self.end):
            self.value += i
        print("end add class")


Add(0, 100).start()
