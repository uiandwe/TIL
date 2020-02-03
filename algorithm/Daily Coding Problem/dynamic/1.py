# -*- coding: utf-8 -*-
"""
You are given a 2-d matrix where each cell represents number of coins in that cell.

Assuming we start at matrix[0][0], and can only move right or down,

find the maximum number of coins you can collect by the bottom right corner.

For example, in this matrix

0 3 1 1
2 0 0 4
1 5 3 1

The most we can collect is 0 + 2 + 1 + 5 + 3 + 1 = 12 coins.


"""


def solution(array):
    m = len(array)
    if m <= 0:
        return 0
    n = len(array[0])

    if n <= 0:
        return 0

    if m == n == 1:
        return array[0][0]

    d = [[0 for x in range(n)] for y in range(m)]

    for y in range(m):
        for x in range(n):
            if y > 0:
                d[y][x] = max(d[y][x], d[y-1][x]+array[y][x])
            if x > 0:
                d[y][x] = max(d[y][x], d[y][x-1]+array[y][x])


    for temp in d:
        print(temp)


map = [[0, 3, 1, 1],
       [2, 0, 0, 4],
       [1, 5, 3, 1]]

solution(map)

