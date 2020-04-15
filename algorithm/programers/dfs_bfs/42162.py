# -*- coding: utf-8 -*-
map = []
d = []
visit = []


def dfs(node, index, connect):
    global visit, map
    if visit[index] == 0:
        visit[index] = 1
        d[index] = connect

    for i, val in enumerate(node):
        if i != index and val == 1 and visit[i] == 0:
            dfs(map[i], i, connect)


def solution(n, computers):
    global map, d, visit

    map = computers
    d = [0 for x in map]
    visit = [0 for x in map]

    for index, val in enumerate(map):
        dfs(val, index, index)

    return len(set(d))



print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
