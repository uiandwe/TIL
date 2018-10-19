# -*- coding: utf8 -*-
'''
입력 1
0 0 1
1 0 1

입력 2
0 0 1
2 0 1
10 0 5
'''
import math

a = []
check = []
group = []


for i in range(2): #입력 2개 일때 
    str = raw_input()
    str = str.split(' ')
    x = str[0]
    y = str[1]
    r = str[2]

    vector = [int(x), int(y), int(r)]
    a.append(vector)
    check.append(0)


print a



def checkCirclePoint(x1, y1, r1, x2, y2, r2):
    dis1 = math.sqrt((x1-x2)*(x1-x2))+((y1-y2)*(y1-y2))
    dis2 = r1+r2
    if dis1 > dis2:
        return False
    else:
        return True


def checkObjInsert(x):
    check = False
    for temp in group:
        if x in temp:
            check = True
    if check is False:
        group.append([x])


def checkObjOrAndInsert(i, j):
    for temp in group:
        if i in temp :
            if j in temp:
                return 0
            else:
                temp.append(j)
                return 0
    group.append([i, j])



for i in range(len(a)):
    for j in range(len(a)):
        if i != j:
            x1 = a[i][0]
            y1 = a[i][1]
            r1 = a[i][2]

            x2 = a[j][0]
            y2 = a[j][1]
            r2 = a[j][2]

            print i, j, checkCirclePoint(x1, y1, r1, x2, y2, r2)

            if checkCirclePoint(x1, y1, r1, x2, y2, r2) :
                checkObjOrAndInsert(i, j)
            else:
                checkObjInsert(i)
                checkObjInsert(j)



print group
