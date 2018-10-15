import sys

d = [0]

coin = [2, 5, 12]


num = input()

for i in range(1, num+1):
    d.append(sys.maxint)

for i in coin:
    for j in range(1, num+1):
        if j-i >= 0 and d[j-i]+1 < d[j]:
            d[j] = d[j-i]+1


print d


