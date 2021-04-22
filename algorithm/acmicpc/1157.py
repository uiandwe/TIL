# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/1157
from collections import Counter

s = input()

d = Counter(s.upper()).most_common(2)

if len(d) > 1 and d[0][1] == d[1][1]:
    print("?")
else:
    print(d[0][0])
