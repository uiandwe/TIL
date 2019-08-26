# -*- coding: utf-8 -*-
# delegating iterations

class Stack(object):
    def __init__(self):
        self.__list = []

    def push(self, val):
        self.__list.append(val)

    def pop(self):
        return self.__list.pop()

    def __iter__(self):
        return iter(self.__list)



s = Stack()
s.push(1)
s.push(2)
for val in s:
    print(val)

