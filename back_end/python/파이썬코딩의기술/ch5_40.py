# -*- coding: utf-8 -*-
def my_coroutin():
    while True:
        received = yield
        print(received)

it = my_coroutin()
next(it)
it.send('first')
it.send('second')

print("=========================================")

def minimize():
    current = yield
    while True:
        value = yield current
        current = min(value, current)

it = minimize()
next(it)
print(it.send(10))
print(it.send(4))
print(it.send(22))


print("==============================================")


class MyReturn(Exception):
    def __init__(self, value):
        self.value = value

def delegated():
    yield 1
    raise MyReturn(2)
    yield 'not'

def composed():
    try:
        for value in delegated():
            yield value
    except MyReturn as e:
        output = e.value
    yield output * 4

print(list(composed()))
