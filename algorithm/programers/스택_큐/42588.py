# -*- coding: utf-8 -*-
class Stack:
    __slots__ = ["array"]

    def __init__(self):
        self.array = []

    def push(self, val):
        self.array.append(val)

    def pop(self):
        if self.empty():
            return -1

        return self.array.pop()

    def empty(self):
        if self.size() > 0:
            return False
        else:
            return True

    def size(self):
        return len(self.array)



def solution(heights):
    result_array = []

    s = Stack()
    for val in heights:
        s.push(val)

    while not s.empty():
        pop = s.pop()
        send = 0
        for i in reversed(range(s.size())):
            if pop < s.array[i]:
                send = i + 1
                break
        result_array.append(send)

    result_array.reverse()
    return result_array





assert solution([6, 9, 5, 7, 4]) == [0, 0, 2, 2, 4]
assert solution([3, 9, 9, 3, 5, 7, 2]) == [0, 0, 0, 3, 3, 3, 6]
assert solution([1, 5, 3, 6, 7, 6, 5]) == [0, 0, 2, 0, 0, 5, 6]

print(solution([6, 9, 5, 7, 4]))
