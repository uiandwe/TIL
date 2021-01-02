# -*- coding: utf-8 -*-

path = [[1, 3, 5, 8],
        [4, 2, 1, 7],
        [4, 3, 2, 3]]
d = [[float('inf') for i in range(4)] for j in range(3)]
d[0][0] = path[0][0]

def minPath1(y, x):
    if y < 0 or x < 0:
        return float('inf')
    if y >= 0 and x >= 0 and d[y][x] != float('inf'):
        return d[y][x]

    d[y][x] = path[y][x] + min(minPath1(y-1, x), minPath1(y, x-1))
    return d[y][x]

minPath1(2, 3)
print(d)
