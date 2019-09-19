# -*- coding: utf-8 -*-
# https://programmers.co.kr/learn/courses/30/lessons/42840?language=python3

from itertools import cycle

def solution(answers):
    answer = []
    correct = [0, 0, 0]
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    # for index, value in enumerate(answers):
    #     if p1[index % len(p1)] == value:
    #         correct[0] += 1
    #     if p2[index % len(p2)] == value:
    #         correct[1] += 1
    #     if p3[index % len(p3)] == value:
    #         correct[2] += 1

    for p1_v, p2_v, p3_v, value in zip(cycle(p1), cycle(p2), cycle(p3), answers):
        if value == p1_v:
            correct[0] += 1
        if value == p2_v:
            correct[1] += 1
        if value == p3_v:
            correct[2] += 1

    max_correct = max(correct)
    for index, value in enumerate(correct):
        if max_correct == value:
            answer.append(index+1)
    return sorted(answer)



def test_solution():
    assert solution([1,2,3,4,5]) == [1]
    assert solution([1, 2, 3, 4, 5, 1]) == [1]
    assert solution([1,3,2,4,2]) == [1,2,3]
    assert solution([1, 3, 2, 4, 2, 1]) == [1]
    assert solution([]) == [1, 2, 3]
    assert solution([3, 3, 1, 1, 2, 2, 4, 4, 5, 5]) == [3]
    assert solution([3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3]) == [3]
    assert solution([4, 4, 4, 5, 1]) == [1, 2, 3]
    assert solution([2, 1, 2, 3, 2, 4, 2]) == [2]


print(solution([1,2,3,4,5, 1, 2]))
