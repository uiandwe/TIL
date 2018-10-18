# -*- coding: utf8 -*-
import queue

q = queue.Queue()

a = [[0, 1, 1, 0, 1, 0, 0],
     [0, 1, 1, 0, 1, 0, 1],
     [1, 1, 1, 0, 1, 0, 1],
     [0, 0, 0, 0, 1, 1, 1],
     [0, 1, 0, 0, 0, 0, 0],
     [0, 1, 1, 1, 1, 1, 0],
     [0, 1, 1, 1, 0, 0, 0]]
d = [[0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0]]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y, cnt):
    q.push([x, y])
    d[x][y] = cnt

    while q.empty() is False:
        xy = q.pop()
        x = xy[0]
        y = xy[1]
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx and nx < 7 and 0 <= ny and ny < 7:
                if a[nx][ny] == 1 and d[nx][ny] == 0:
                    q.push([nx, ny])
                    d[nx][ny] = cnt

cnt = 0
for i in range(7):
    for j in range(7):
        if a[i][j] == 1 and d[i][j] == 0:
            cnt += 1
            dfs(i, j, cnt)

for i in d:
    print i
