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

from collections import deque

q = deque()


def bfs(v):
    q.append(v)
    visited[v] = True

    while q:
        node = q.popleft()
        print(node, end=' ')
        for i in graph[node]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


bfs(1)
