# -*- coding: utf-8 -*-
import heapq


def check_move(y, x, n, visite):
    if 0 <= y < n and 0 <= x < n and visite[y][x] == False:
        return True
    return False


def solution(land, height):
    N = len(land)

    visit = [[False] * N for _ in range(N)]
    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    q = []

    q.append((0, 0, 0))
    visite_count = 0
    max_count = N * N
    value = 0

    while visite_count < max_count:
        v, y, x = heapq.heappop(q)
        # print(q)

        if visit[y][x]:
            continue
        visit[y][x] = True

        visite_count += 1
        value += v

        c_height = land[y][x]
        for ay, ax in move:
            ny, nx = y + ay, x + ax
            if check_move(ny, nx, N, visit):
                n_height = land[ny][nx]

                if abs(n_height - c_height) > height:
                    heapq.heappush(q, (abs(n_height - c_height), ny, nx))
                else:
                    heapq.heappush(q, (0, ny, nx))
    return value


solution([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]], 3) == 15
solution([[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]], 1)
