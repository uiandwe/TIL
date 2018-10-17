# -*- coding: utf8 -*-



d = []
a = [10, -4, 3, 1, 5, 6, -35, 12, 21, -1]

d.append(a[0])

for i in range(1, len(a)):
     d.append(max(d[i-1]+a[i], a[i]))

print d
