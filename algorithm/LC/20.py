# -*- coding: utf-8 -*-
class Stack:
    def __init__(self):
        self.array = []

    def push(self, value):
        self.array.append(value)

    def pop(self):
        if not self.empty():
            return self.array.pop()
        return None

    def size(self):
        return len(self.array)

    def empty(self):
        return False if self.size() > 0 else True


class Solution:
    def isValid(self, s: str) -> bool:
        stack = Stack()
        for v in s:
            if v == '(' or v == '[' or v == '{':
                stack.push(v)
            else:
                temp = stack.pop()
                if (temp == '(' and v == ')') or (temp == '[' and v == ']') or (temp == '{' and v == '}'):
                    continue
                else:
                    return False

        return stack.empty()


