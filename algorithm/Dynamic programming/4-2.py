# -*- coding: utf-8 -*-
path = [[1, 3, 5, 8],
        [4, 2, 1, 7],
        [4, 3, 2, 3]]
d = [[float('inf') for i in range(4)] for j in range(3)]
d[0][0] = path[0][0]

for i in range(1, len(path)):
    d[i][0] = path[i][0] + d[i-1][0]

for i in range(1, len(path[0])):
    d[0][i] = path[0][i] + d[0][i-1]


def minPath(y, x):

    if y >= 0 and x >= 0 and d[y][x] != float('inf'):
        return d[y][x]

    d[y][x] = min(minPath(y-1, x-1), minPath(y-1, x), minPath(y, x-1)) + path[y][x]

    return d[y][x]

print(minPath(2, 3))
print(d)
