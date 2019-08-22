# -*- coding: utf-8 -*-
def solution(arr):
    answer = []

    if len(arr) > 0:
        answer.append(arr[0])

        for i in range(1, len(arr)):
            if answer[-1] != arr[i]:
                answer.append(arr[i])
    return answer


def test_solution():
    assert solution([1, 1, 3, 3, 0, 1, 1]) == [1, 3, 0, 1]
    assert solution([4, 4, 4, 3, 3]) == [4, 3]
    assert solution([]) == []
    assert solution([1, 2]) == [1, 2]
    assert solution([3]) == [3]


print(solution([1, 1, 3, 3, 0, 1, 1]))

