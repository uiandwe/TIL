# -*- coding: utf-8 -*-
def solution(citations):
    for index, value in enumerate(sorted(citations)):
        print(index, value)
        if value >= len(citations)-index:
            return len(citations)-index
    return 0

def test_solution():
    assert solution([3, 0, 6, 1, 5]) == 3
    assert solution([3, 0, 6, 1, 5, 4, 7]) == 4
    assert solution([0, 1]) == 1
    assert solution([22, 44]) == 2


print(solution([3, 0, 6, 1, 5]))
