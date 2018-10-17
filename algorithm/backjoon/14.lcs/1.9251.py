# -*- coding: utf8 -*-



a = "ACAYKP"
b = "CAPCAK"


for index, i in enumerate(a):
     temp = i
     for j in a[index+1:len(a)]:
          temp += j
          if temp in b:
               print("Okay", temp)


d = []
maxLen = max(len(a), len(b))
for i in range(maxLen+1):
     temp = []
     for j in range(maxLen+1):
          temp.append(0)
     d.append(temp)


for i in range(1, len(a)+1):
     for j in range(1, len(b)+1):
          if a[i-1] == b[j-1]:
               d[i][j] = d[i-1][j-1]+1
          else:
               d[i][j] = max(d[i][j-1], d[i-1][j])

for i in d:
     print i
