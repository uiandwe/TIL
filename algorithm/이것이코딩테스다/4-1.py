# -*- coding: utf-8 -*-

n = int(input())
point = [1, 1]
plans = input().split()

# print(n, plans)
d = {
    'R' : (0, 1),
    'L' : (0, -1),
    'U': (-1, 0),
    'D': (1, 0)
}

for p in plans:
    if 0 < point[0]+d[p][0] < n and 0 < point[1]+d[p][1] < n:
        point[0] += d[p][0]
        point[1] += d[p][1]

print(point)

"""
5
R R R U D D
[3, 4]
# 지도가 반대로 되어 있어 
#U 가 -1 D가 +1이 된다. 
"""
