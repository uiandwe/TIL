# -*- coding: utf-8 -*-
n = int(input())
array = list(map(int, input().split()))


d = [0] * n
d[0] = array[0]
d[1] = array[1]
for i in range(2, len(array)):
    d[i] = max(d[i-1], d[i-2]+array[i])

print(d)

