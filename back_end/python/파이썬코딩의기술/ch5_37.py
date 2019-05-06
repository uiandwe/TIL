# -*- coding: utf-8 -*-
import subprocess
from time import time

def factorize(number):
    for i in range(1, number + 1):
        if number % i == 0:
            yield i


numbers = [2139079, 1214759, 1516637, 1852289]
start = time()
for number in numbers:
    list(factorize(number))

end = time()
print(end-start)


# 스레드로 해도 별로 뺘르지가 않다. GIL 때문에...
from threading import Thread

class FactorizeThread(Thread):
    def __init__(self, number):
        super().__init__()
        self.number = number

    def run(self):
        self.factors = list(factorize(self.number))


start = time()
threads = []
for number in numbers:
    thread = FactorizeThread(number)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

end = time()
print(end-start)


import select

def slow_systemcall():
    select.select([], [], [], 0.1)

start = time()
for _ in range(5):
    slow_systemcall()
end = time()
print(end-start)


start = time()
threads = []
for _ in range(5):
    thread = Thread(target=slow_systemcall)
    thread.start()
    threads.append(thread)

end = time()
print(end-start)
