import sys

coin = [1, 5, 12]

d = [1]


num1 = input()


for i in range(1, num1+1):
    d.append(sys.maxint)


for i in coin:
    for j in range(i, len(d)):
        # if j-i >= 0:
        d[j] = min(d[j], d[j-i]+1)


print d
