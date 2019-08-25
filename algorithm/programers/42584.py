# -*- coding: utf-8 -*-

class Stack(object):
    def __init__(self):
        self._stack_array = []

    def push(self, value, index):
        self._stack_array.append([value, index])

    def pop(self):
        if len(self._stack_array) > 0:
            return self._stack_array.pop(len(self._stack_array)-1)
        return []

    def top(self):
        if len(self._stack_array) > 0:
            return self._stack_array[-1]
        else:
            return [0, 0]

    @property
    def array(self):
        return self._stack_array


def solution(prices):
    answer = [0 for i in prices]

    s = Stack()
    s.push(prices[0], 0)
    for index in range(1, len(prices)):
        value = prices[index]
        while s.top()[0] > value:
            temp = s.pop()
            answer[temp[1]] = index - temp[1]
        s.push(value, index)

    for value in s.array:
        answer[value[1]] = (len(prices)-1) - value[1]

    return answer


def test_solution():
    assert solution([1, 2, 3, 2, 3]) == [4, 3, 1, 1, 0]
    assert solution([1, 3, 3, 2, 3]) == [4, 2, 1, 1, 0]
    assert solution([1, 2, 3]) == [2, 1, 0]
    assert solution([1, 2]) == [1, 0]
    assert solution([2, 1]) == [1, 0]


print(solution([2, 1]))
