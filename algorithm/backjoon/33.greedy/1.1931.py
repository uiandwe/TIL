# -*- coding: utf8 -*-

a = []
d = []


for i in range(11):
    str = raw_input()
    str = str.split(' ')
    startTime = str[0]
    endTime = str[1]

    vector = [int(startTime), int(endTime)]
    a.append(vector)

a.sort(key=lambda x: x[1])
print a

d.append(a[0])

for i in a:
    temp = d[len(d)-1]
    if i[0] != temp[0] and i[1] != temp[1] and temp[1] <= i[0]:
        d.append(i)

print d
