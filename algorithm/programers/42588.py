# -*- coding: utf-8 -*-
# https://programmers.co.kr/learn/courses/30/lessons/42588


class Stack(object):
    def __init__(self):
        self._stack_array = []
        self._response_array = [0]

    def push(self, value):
        self._stack_array.append(value)
        if len(self._stack_array) > 1:
            for i, e in reversed(list(enumerate(self._stack_array))):
                if e > value:
                    self._response_array.append(i+1)
                    break
            else:
                self._response_array.append(0)

    @property
    def tower(self):
        return self._response_array


def solution(heights):
    s = Stack()
    for val in heights:
        s.push(val)

    return s.tower


def test_solution():
    assert solution([6, 9, 5, 7, 4]) == [0, 0, 2, 2, 4]
    assert solution([3, 9, 9, 3, 5, 7, 2]) == [0, 0, 0, 3, 3, 3, 6]
    assert solution([1, 5, 3, 6, 7, 6, 5]) == [0, 0, 2, 0, 0, 5, 6]

print(solution([6, 9, 5, 7, 4]))
