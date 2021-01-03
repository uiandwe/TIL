# -*- coding: utf-8 -*-

path = [[1, 3, 5, 8],
        [4, 2, 1, 7],
        [4, 3, 2, 3]]
d = [[float('inf') for i in range(4)] for j in range(3)]
d[0][0] = path[0][0]

def minPath3(y, x):
    if y < 0 or x < 0:
        return float('inf')
    if y >= 0 and x >= 0 and d[y][x] != float('inf'):
        return d[y][x]

    d[y][x] = path[y][x] + min(minPath3(y-1, x), minPath3(y, x-1))
    return d[y][x]

minPath3(2, 3)
print(d)

def minPath1(y, x):
    if y == 0 and x ==0:
        return path[0][0]
    if y == 0:
        return minPath1(0, x-1) + path[0][x]
    if x == 0:
        return minPath1(y-1, 0) + path[y][0]

    v1 = minPath1(y-1, x)
    v2 = minPath1(y, x-1)
    return min(v1, v2) + path[y][x]

print(minPath1(2, 3))

memo = [[float('inf') for i in range(4)] for j in range(3)]

def minPath2(y, x):

    if memo[y][x] != float('inf'):
        return memo[y][x]

    if y == 0 and x ==0:
        memo[y][x] = path[0][0]
    elif y == 0:
        memo[y][x] =  minPath1(0, x-1) + path[0][x]
    elif x == 0:
        memo[y][x] =  minPath1(y-1, 0) + path[y][0]
    else:
        v1 = minPath1(y-1, x)
        v2 = minPath1(y, x-1)
        memo[y][x] = min(v1, v2) + path[y][x]
    return memo[y][x]


print(minPath1(2, 3))
