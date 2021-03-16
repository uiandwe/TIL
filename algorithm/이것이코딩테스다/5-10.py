# -*- coding: utf-8 -*-
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

next_x = [0, 0, -1, 1]
next_y = [1, -1, 0, 0]


def dfs(y, x):
    if 0 <= y < n and 0 <= x < m and graph[y][x] == 0:
        graph[y][x] = 1
        for p in range(4):
            temp_y = next_y[p] + y
            temp_x = next_x[p] + x
            dfs(temp_y, temp_x)
    return True


result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            dfs(i, j)
            result += 1

print(result)
"""
3 3
001
010
101
3
"""

"""

4 5
00110
00011
11111
00000
3
"""
