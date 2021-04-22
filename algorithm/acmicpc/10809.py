# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/10809


s = input()

d = [-1 for _ in range(26)]


for i, c in enumerate(s):
    p = ord(c)-97
    if d[p] == -1:
        d[p] = i

for item in d:
    print(item, end=' ')
