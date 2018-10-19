# -*- coding: utf8 -*-
import time
start_time = time.time()

a = [[-1, 1, 0, 0, 0, 0],
     [0, -1, -1, -1, -1, 0],
     [0, -1, 0, 0, -1, 0],
     [0, -1, 0, 0, -1, 0],
     [0, -1, -1, -1, -1, 0],
     [0, 0, 0, 0, 0, 0]]

d = [[0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0]]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y, cnt):
    if a[x][y] == 0 or a[x][y] > cnt:
        a[x][y] = cnt

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx and nx < 6 and 0 <= ny and ny < 6:
            if a[nx][ny] == 0 or (a[nx][ny] > 0 and a[nx][ny] > cnt+1):
                bfs(nx, ny, cnt+1)



for i in range(6):
    for j in range(6):
        if a[i][j] == 1:
            bfs(i, j, 1)

for i in a:
    print i

print("--- %s seconds ---" %(time.time() - start_time))
