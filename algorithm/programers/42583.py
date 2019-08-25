# -*- coding: utf-8 -*-
class Queue(object):
    def __init__(self, length):
        self._queue_array = [0 for i in range(length)]

    def push(self, value):
        self._queue_array.append(value)

    def pop(self):
        return self._queue_array.pop(0)

    def first(self):
        if self.length() > 0:
            return self._queue_array[0]
        else:
            return 0

    def length(self):
        return len(self._queue_array)

    def sum(self):
        return sum(self._queue_array)

    @property
    def queue_array(self):
        return self._queue_array


def solution(bridge_length, weight, truck_weights):

    q = Queue(bridge_length)

    answer = 0
    while len(truck_weights) > 0:
        answer += 1
        q.pop()

        push_value = 0
        if q.sum() + truck_weights[0] <= weight:
            push_value = truck_weights.pop(0)
        q.push(push_value)

    if q.sum() > 0:
        max = 0
        for index, val in enumerate(q.queue_array):
            if val > 0:
                max = index+1
        answer += max

    return answer


def test_solution():
    assert solution(2, 10, [7,4,5,6]) == 8
    assert solution(100, 100, [10]) == 101
    assert solution(100, 100, [10,10,10,10,10,10,10,10,10,10]) == 110

print(solution(2, 10, [7,4,5,6]))
