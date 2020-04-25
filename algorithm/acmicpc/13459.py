# -*- coding: utf-8 -*-

from collections import deque
from sys import stdin

input = stdin.readline

n, m = list(map(int, input().split(" ")))
map = []

for i in range(n):
    temp = list(input())
    map.append(temp)

visited = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
ry, rx, by, bx = 0, 0, 0, 0

for y in range(n):
    for x in range(m):
        if map[y][x] == 'R':
            ry = y
            rx = x
        if map[y][x] == 'B':
            by = y
            bx = x

visited[ry][rx][by][bx] = True
q = deque()
q.append((ry, rx, by, bx, 1))

x_position = [1, -1, 0, 0]
y_position = [0, 0, 1, -1]


def ball_move(y, x, dy, dx):
    count = 0
    while map[dy+y][dx+x] != '#' and map[dy][dx] != 'O':
        dy += y
        dx += x
        count += 1

    return dy, dx, count


def bfs():
    while q:
        ry, rx, by, bx, count = q.popleft()

        if count > 10:
            break

        for i in range(4):
            next_y = y_position[i]
            next_x = x_position[i]

            next_ry, next_rx, r_move_count = ball_move(next_y, next_x, ry, rx)
            next_by, next_bx, b_move_count = ball_move(next_y, next_x, by, bx)

            if map[next_by][next_bx] == 'O':
                continue
            if map[next_ry][next_rx] == 'O':
                print(1)
                return

            if next_ry == next_by and next_rx == next_bx:
                if r_move_count > b_move_count:
                    next_ry -= next_y
                    next_rx -= next_x
                else:
                    next_by -= next_y
                    next_bx -= next_x

            if not visited[next_ry][next_rx][next_by][next_bx]:
                visited[next_ry][next_rx][next_by][next_bx] = True
                q.append((next_ry, next_rx, next_by, next_bx, count+1))

    print(0)

bfs()
