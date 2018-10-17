# -*- coding: utf8 -*-

num = input()

d = [1, 1, 1]


for i in range(3, num):
     d.append(d[i-2]+d[i-3])

print d
