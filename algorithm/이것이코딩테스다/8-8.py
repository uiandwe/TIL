# -*- coding: utf-8 -*-
n, money = list(map(int, input().split(' ')))
tokens = list(map(int, input().split()))

d = [float('inf')] * (money+1)
d[0] = 0
for i in range(1, money+1):
    for t in tokens:
        if i >= t:
            d[i] = min(d[i], d[i-t]+1)
print(d)

"""
2 15
2 3
[0, inf, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]
"""
"""
3 4
3 5 7
[0, inf, inf, 1, inf]
"""
