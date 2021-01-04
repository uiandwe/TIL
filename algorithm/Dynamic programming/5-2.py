# -*- coding: utf-8 -*-
def num_of_paths(m, n):
    if m == 0 and n == 0:
        return 0
    if m == 1 or n == 1:
        return 1

    return num_of_paths(m-1, n) + num_of_paths(m, n-1)


print(num_of_paths(3, 4))



def num_of_path_memo(m, n):
    d = [[0 for i in range(n)] for j in range(m)]

    for y in range(m):
        d[y][0] = 1
    for x in range(n):
        d[0][x] = 1


    for y in range(1, m):
        for x in range(1, n):
            d[y][x] = d[y-1][x] + d[y][x-1]

    print(d[m-1][n-1])

num_of_path_memo(3, 4)


