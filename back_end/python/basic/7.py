# -*- coding: utf-8 -*-
# in operation

class Stack:
    def __init__(self):
        self.__list = []

    def push(self, val):
        self.__list.append(val)

    def pop(self):
        return self.__list.pop()

    def __contains__(self, item):
        return True if item in self.__list else False


stack = Stack()
stack.push(1)
print(1 in stack)
print(2 in stack)
