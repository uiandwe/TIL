# -*- coding: utf-8 -*-

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * len(graph)


def dfs(v):
    if not visited[v]:
        print(v, end=' ')
        visited[v] = True
        for i in graph[v]:
            dfs(i)


dfs(1)
