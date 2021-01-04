# -*- coding: utf-8 -*-
import collections

def num_of_path_broken(m, n, arr):
    d = [[0 for i in range(n)] for j in range(m)]

    for i in range(m):
        d[i][0] = 1

    for i in range(n):
        d[0][i] = 1

    broken = collections.Counter(arr)

    for y in range(1, m):
        for x in range(1, n):
            if (x, y-1, x, y) not in broken:
                d[y][x] += d[y-1][x]
            if (x-1, y, x, y) not in broken:
                d[y][x] += d[y][x-1]

    print(d)
    print(broken)



num_of_path_broken(4, 5, [(2, 1, 3, 1), (1, 2, 2, 2), (2, 2, 3, 2), (3, 3, 4, 3)])

