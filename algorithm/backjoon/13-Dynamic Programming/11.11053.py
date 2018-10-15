# -*- coding: utf8 -*-



d = [1, 1, 1, 1, 1, 1]
a = [10, 20, 10, 30, 20, 50]

for i in range(len(a)):
     for j in range(0, i):
          if a[j] < a[i] and d[i] < d[j]+1:
               d[i] = d[j]+1

print d
