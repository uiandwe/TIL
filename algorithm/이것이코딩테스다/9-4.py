# -*- coding: utf-8 -*-
n = int(input())
m = int(input())

graph = [[float('inf')] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

x, k = map(int, input().split())

for a in graph:
    print(a)
print(graph[1][k] + graph[k][x])
"""
5
7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
[inf, inf, inf, inf, inf, inf]
[inf, 0, 1, 1, 1, 2]
[inf, 1, 0, 2, 1, 2]
[inf, 1, 2, 0, 1, 1]
[inf, 1, 1, 1, 0, 1]
[inf, 2, 2, 1, 1, 0]
3
"""
