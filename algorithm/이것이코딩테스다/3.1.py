# -*- coding: utf-8 -*-
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

first = data[n-1]
second = data[n-2]
result = []
for i in range(m):
    if i != 0 and i % k == 0:
        result.append(second)
    else:
        result.append(first)

print(sum(result))
"""
5 8 3
2 4 5 4 6
6+6+6+5+6+6+6+5 
result = 46


5 7 2
3 4 3 4 3
4+4+4+4+4+4+4
result = 28
"""
