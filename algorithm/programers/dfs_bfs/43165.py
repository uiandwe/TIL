# -*- coding: utf-8 -*-
answer = 0

def DFS(idx, numbers, target, value):
    global answer
    n = len(numbers)
    if idx == n and target == value:
        answer += 1
        return

    if idx == n:
        return

    DFS(idx+1, numbers, target, value+numbers[idx])
    DFS(idx+1, numbers, target, value-numbers[idx])


def solution(numbers, target):
    global answer
    DFS(0, numbers, target, 0)
    return answer


print(solution([1, 1, 1], 3))


