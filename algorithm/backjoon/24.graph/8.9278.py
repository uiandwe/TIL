# -*- coding: utf8 -*-

import time
start_time = time.time()

a = [[1, 1, 0, 1, 1, 0],
     [1, 1, 0, 0, 1, 0],
     [1, 1, 0, 0, 1, 0],
     [1, 1, 0, 0, 1, 0],
     [1, 1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1, 1]]

d = [[0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0]]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y, cnt):
    d[x][y] = cnt

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx and nx < 6 and 0 <= ny and ny < 6:
            if a[nx][ny] == 1 and (d[nx][ny] == 0 or d[nx][ny] > cnt+1):
                bfs(nx, ny, cnt+1)




bfs(0, 0, 1)

for i in d:
    print i

print("--- %s seconds ---" %(time.time() - start_time))
