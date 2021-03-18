# -*- coding: utf-8 -*-
n = int(input())
m = int(input())

graph = [[float('inf')] * (n + 1) for _ in range(n + 1)]
print(graph)
for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in graph:
    print(a)

"""
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4 
4 3 2
[inf, inf, inf, inf, inf]
[inf, 0, 4, 8, 6]
[inf, 3, 0, 7, 9]
[inf, 5, 9, 0, 4]
[inf, 7, 11, 2, 0]
"""
