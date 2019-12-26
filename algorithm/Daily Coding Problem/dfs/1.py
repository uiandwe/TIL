# -*- coding: utf-8 -*-
"""
Given a matrix of 1s and 0s, return the number of "islands" in the matrix.

A 1 represents land and 0 represents water,

 so an island is a group of 1s that are neighboring whose perimeter is surrounded by water.

For example, this matrix has 4 islands.

1 0 0 0 0
0 0 1 1 0
0 1 1 0 0
0 0 0 0 0
1 1 0 0 1
1 1 0 0 1

"""

def dfs(arr, y, x, k):

    if arr[y][x] == 0:
        return
    elif arr[y][x] == 1:
        h = len(arr)
        w = len(arr[0])

        arr[y][x] = k

        pos_x = [1, -1, 0, 0]
        pos_y = [0, 0, 1, -1]

        for next_i in range(4):
            next_x = x+pos_x[next_i]
            next_y = y+pos_y[next_i]
            if next_x >=0 and next_x < w and next_y >= 0 and next_y < h:
                dfs(arr, next_y, next_x, k)
    return


def set_island_cnt(arr):
    h = len(arr)
    w = len(arr[0])
    cnt = 2

    for y in range(h):
        for x in range(w):
            if arr[y][x] == 1:
                dfs(arr, y, x, cnt)
                cnt += 1

    return cnt - 2


arr = [[1, 0, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [1, 1, 0, 0, 1],
        [1, 1, 0, 0, 1]]


assert set_island_cnt(arr) == 4
