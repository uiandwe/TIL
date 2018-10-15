# -*- coding: utf8 -*-



d = [1, 100, 2, 50, 60, 3, 5, 6, 7, 8]
a = [1, 100, 2, 50, 60, 3, 5, 6, 7, 8]

for i in range(len(a)):
     for j in range(0, i):
          if a[j] < a[i] and d[i] < d[j]+a[i]:
               d[i] = d[j]+a[i]

print d
