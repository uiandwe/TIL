# -*- coding: utf-8 -*-
def solution(array, commands):
    answer = []
    for c in commands:
        start, end, k = c
        temp = sorted(array[start-1:end])
        answer.append(temp[k-1])
    return answer


def test_solution():
    assert solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]) == [5, 6, 3]


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
