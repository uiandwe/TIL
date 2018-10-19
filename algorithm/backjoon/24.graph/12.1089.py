# -*- coding: utf8 -*-

import time
start_time = time.time()

a = [[2, 3, 3, 1],
     [1, 2, 1, 3],
     [1, 2, 3, 1],
     [3, 1, 1, 0]]

a = [[1, 1, 1, 1],
     [1, 1, 1, 1],
     [1, 1, 1, 1],
     [1, 1, 1, 0]]

a = [[2, 1, 2, 1],
     [1, 2, 1, 2],
     [2, 1, 1, 1],
     [1, 2, 1, 0]]

d = [[0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0]]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y, cnt):
    d[x][y] = cnt

    if a[x][y] == 0:
        return 0

    for i in range(4):
        nx = x+(dx[i]*a[x][y])
        ny = y+(dy[i]*a[x][y])
        if 0 <= nx and nx < 4 and 0 <= ny and ny < 4:
            if d[nx][ny] == 0 or d[nx][ny] > cnt+1:
                bfs(nx, ny, cnt+1)




bfs(0, 0, 1)

for i in d:
    print i

print("--- %s seconds ---" %(time.time() - start_time))
