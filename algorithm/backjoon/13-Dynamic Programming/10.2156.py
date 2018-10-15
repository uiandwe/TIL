# -*- coding: utf8 -*-


d = [0]

a = [0, 6, 10, 13, 9, 8, 1]

d.append(a[1])  #0번째 셋팅
d.append(d[1]+ a[2]) #1번째 셋팅

for i in range(3, len(a)):
    d.append(max(d[i-3]+a[i-1]+a[i], d[i-2]+a[i], d[i-1]))



print d
