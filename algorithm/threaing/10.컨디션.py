# -*- coding: utf-8 -*-
import threading
import time
import random



class Publisher(threading.Thread):
    def __init__(self, i, c):
        self.i = i
        self.c = c
        threading.Thread.__init__(self)

    def run(self):
        while True:
            i = random.randint(0, 1000)
            self.c.acquire()
            print("condition acquired by publisher: {}".format(self.name))
            self.i.append(i)
            self.c.notify()
            print("condition released by publisher: {}".format(self.name))
            self.c.release()
            time.sleep(1)


class Subscriber(threading.Thread):
    def __init__(self, i, c):
        self.i = i
        self.c = c
        threading.Thread.__init__(self)

    def run(self):
        while True:
            self.c.acquire()
            print("condition acquired by comsumer: {}".format(self.name))
            while True:
                if self.i:
                    i = self.i.pop()
                    print("{} pop from list by comsumer: {}".format(i, self.name))
                    break
                print("condition wait by {}".format(self.name))
                self.c.wait()

            print("consumer {} releaseing condition".format(self.name))
            self.c.release()

if __name__ == '__main__':
    i = []
    c = threading.Condition()

    pub1 = Publisher(i, c)
    pub1.start()

    sub1 = Subscriber(i, c)
    sub2 = Subscriber(i, c)

    sub1.start()
    sub2.start()

    pub1.join()
    sub1.join()
    sub2.join()


