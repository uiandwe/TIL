# -*- coding: utf-8 -*-
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.array = []

    def push(self, x: int) -> None:
        self.array.append(x)
        return "null"

    def pop(self) -> None:
        if not self.empty():
            return self.array.pop(len(self.array)-1)
        return "null"

    def top(self) -> int:
        if not self.empty():
            return self.array[len(self.array)-1]
        return "null"

    def getMin(self) -> int:
        if not self.empty():
            min_value = min(self.array)
            return self.array[self.array.index(min_value)]
        return "null"

    def empty(self):
        if len(self.array) > 0:
            return False
        return True

ms = None
answer = []
array1 = ["MinStack","push","push","push","getMin","top","pop","getMin"]
array2 = [[],[-2],[0],[-1],[],[],[],[]]

for a1, a2 in zip(array1, array2):
    if a1 == "MinStack":
        ms = MinStack()
        answer.append("null")
    elif a1 == "push":
        ms.push(a2[0])
        answer.append("null")
    elif a1 == "pop":
        param = ms.pop()
        answer.append("null")
    elif a1 == "top":
        param = ms.top()
        answer.append(param)
    elif a1 == "getMin":
        param = ms.getMin()
        answer.append(param)


print(answer)
