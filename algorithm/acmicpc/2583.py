# -*- coding: utf-8 -*-
from typing import List


def dfs(y: int, x: int, d: List[List[int]], g: int):
    d[y][x] = g

    h = len(d)
    w = len(d[0])

    x_position = [1, -1, 0, 0]
    y_position = [0, 0, 1, -1]

    for i in range(4):
        next_x = x + x_position[i]
        next_y = y + y_position[i]

        if 0 <= next_x < w and 0 <= next_y < h:
            if d[next_y][next_x] == 0:
                dfs(next_y, next_x, d, g)


def solution(M: int, N: int, array: List[List[int]]):
    d = [[0 for x in range(N)] for y in range(M)]
    for node in array:
        y1 = node[0]
        x1 = node[1]
        y2 = node[2]
        x2 = node[3]
        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                d[y][x] = -1

    group = 1
    for y in range(M):
        for x in range(N):
            if d[y][x] == 0:
                dfs(y, x, d, group)
                group += 1

    for i in d:
        print(i)


solution(5, 7, [[0, 1, 3, 1], [1, 0, 2, 3], [3, 4, 4, 5]])
