# -*- coding: utf-8 -*-
n = 5
a = [10, 20, 30, 40, 50]


summary = 0
d = [0 for _ in range(len(a))]
for i in range(len(a)):
    summary += a[i]
    d[i] = summary

left = 3
right = 5
print(a)
print(d)
print(d[right-1] - d[left-1])
