# -*- coding: utf8 -*-

a = [0, 3, 1, 4, 3, 2]

a.sort()

print a

d = [0]

for i in range(1, len(a)):
    d.append(d[i-1] + a[i])


print d
print sum(d)
