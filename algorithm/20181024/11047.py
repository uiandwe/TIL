import sys

coin = [1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000]

d = [1]


num1 = input()


for i in range(1, num1+1):
    d.append(sys.maxint)


for i in coin:
    for j in range(i, len(d)):
        d[j] = min(d[j], d[j-i]+1)


print d[4200]
