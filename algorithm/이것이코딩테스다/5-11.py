# -*- coding: utf-8 -*-
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

next_x = [0, 0, -1, 1]
next_y = [1, -1, 0, 0]

from collections import deque

q = deque()
q.append((0, 0, 1))
result = float('inf')
while q:
    node = q.popleft()
    y = node[0]
    x = node[1]
    count = node[2]
    if y == n-1 and x == m-1:
        result = min(result, count)

    graph[y][x] = 0

    for i in range(4):
        temp_y = next_y[i] + y
        temp_x = next_x[i] + x
        if 0 <= temp_y < n and 0 <= temp_x < m and graph[temp_y][temp_x] == 1:
            q.append((temp_y, temp_x, count+1))


print(result)
"""
3 3
110
010
011
5
"""

"""
5 6
101010
111111
000001
111111
111111
10
"""
