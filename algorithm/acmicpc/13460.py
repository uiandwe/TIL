# -*- coding: utf-8 -*-
from collections import deque

n, m = list(map(int, input().split(" ")))

map = []
for i in range(n):
    temp = list(input())
    map.append(temp)

visited = [[[[False] * m for _ in range(n)]for _ in range(m)]for _ in range(n)]

ry, rx, by, bx = 0, 0, 0, 0

for h in range(n):
    for w in range(m):
        if map[h][w] == 'R':
            ry = h
            rx = w
        if map[h][w] == 'B':
            by = h
            bx = w

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
            next_x = x_position[i]
            next_y = y_position[i]

            r_next_y, r_next_x, r_move_count = ball_move(next_y, next_x, ry, rx)
            b_next_y, b_next_x, b_move_count = ball_move(next_y, next_x, by, bx)

            if map[b_next_y][b_next_x] == 'O':
                continue

            if map[r_next_y][r_next_x] == 'O':
                print(count)
                return

            if r_next_y == b_next_y and r_next_x == b_next_x:
                if r_move_count > b_move_count:
                    r_next_y -= next_y
                    r_next_x -= next_x
                else:
                    b_next_y -= next_y
                    b_next_x -= next_x

            if not visited[r_next_y][r_next_x][b_next_y][b_next_x]:
                visited[r_next_y][r_next_x][b_next_y][b_next_x] = True
                q.append((r_next_y, r_next_x, b_next_y, b_next_x, count+1))

    print(-1)

bfs()
