# -*- coding: utf-8 -*-
def minPath(n):
    d = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        d[i][0] = 1
        d[0][i] = 1

    for y in range(1, n):
        for x in range(1, n):
            d[y][x] = d[y-1][x] + d[y][x-1]

    print(d)

def minPathDp(y, x):
    if y == 1 or x == 1:
        return 1

    return minPathDp(y-1, x) + minPathDp(y, x-1)

minPath(4)

print(minPathDp(4, 4))

minPath(5)

print(minPathDp(5, 5))
