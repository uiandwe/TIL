# -*- coding: utf8 -*-
import sys


coin = [1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000]
d = [0]

num1 = input()

for i in range(num1+1):
    d.append(sys.maxint)

for i in coin:
    for j in range(i, num1+1):
        d[j] = min(d[j], d[j-i]+1)

print d[num1]
