# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import collections


class Queue(object):
    def __init__(self, length):
        self._queue_array = collections.deque([0 for i in range(length)])
        self._sum = 0

    def push(self, value):
        self._queue_array.append(value)
        self._sum += value

    def pop(self):
        self._sum -= self._queue_array.popleft()

    def length(self):
        return len(self._queue_array)

    def sum(self):
        return sum(self._queue_array)

    @property
    def queue_array(self):
        return self._queue_array

    @property
    def total(self):
        return self._sum


def solution(bridge_length, weight, truck_weights):

    q = Queue(bridge_length)

    answer = 0
    while truck_weights:
        answer += 1
        q.pop()

        push_value = 0
        if q.total + truck_weights[0] <= weight and q.length() <= bridge_length:
            push_value = truck_weights.pop(0)
        q.push(push_value)

    answer += q.length()

    return answer


def test_solution():
    assert solution(2, 10, [7,4,5,6]) == 8
    assert solution(100, 100, [10]) == 101
    assert solution(100, 100, [10,10,10,10,10,10,10,10,10,10]) == 110

print(solution(2, 10, [7,4,5,6]))

