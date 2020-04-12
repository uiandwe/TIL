# -*- coding: utf-8 -*-
"""
1,2,3,5,6,8,9가
주어졌다
문자열로묶어라
ex
1~3, 5~6, 8~9
"""

class Queue:
    __slots__ = ['array']

    def __init__(self):
        self.array = []

    def size(self):
        return len(self.array)

    def empty(self):
        return True if self.size() <= 0 else False

    def push(self, value):
        self.array.append(value)

    def pop(self):
        if self.empty() is False:
            return self.array.pop(0)
        return -1

    def last(self):
        if self.empty() is False:
            return self.array[self.index()]
        return -1

    def first(self):
        if self.empty() is False:
            return self.array[0]
        return -1

    def index(self):
        return self.size()-1

    def flush(self):
        self.array = []


def solution(arr):
    ret_arr = []

    q = Queue()
    q.push(arr.pop(0))

    for n in arr:
        if q.last()+1 != n:
            ret_arr.append([q.first(), q.last()])
            q.flush()
            q.push(n)
        else:
            q.push(n)

    ret_arr.append([q.first(), q.last()])

    print(",".join(str(x[0])+"~"+str(x[1]) for x in ret_arr))


solution([1,2,3,5,6,8,9])
