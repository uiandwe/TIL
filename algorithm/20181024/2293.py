import sys

coin = [1, 2, 5]

d = [1]


num1 = input()


for i in range(1, num1+1):
    d.append(0)


for i in coin:
    for j in range(i, len(d)):
        # if j-i >= 0:
        d[j] += d[j-i]


print d
