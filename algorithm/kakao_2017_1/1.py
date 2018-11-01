https://programmers.co.kr/learn/courses/30/lessons/1829

# -*- coding: utf8 -*-
import queue

q = queue.Queue()

a = []
d = []
relation = [[1, 1, 1, 0], [1, 2, 2, 0], [1, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 3], [0, 0, 0, 3]]
size_m = 6
size_n = 4
groupMaxCount = 0

x_pos = [0, 0, -1, 1]
y_pos = [1, -1, 0, 0]

#초기화 부분
for i in relation:
    a.append(i)

for i in range(6):
    temp = []
    for j in range(4):
        temp.append(0)
    d.append(temp)

for i in range(6):
    temp = []
    for j in range(4):
        temp.append(0)
#########

def dfs(x, y, vlaue, cnt):
    global groupMaxCount
    q.push([x, y])
    d[x][y] = cnt
    count = 0

    while q.empty() is False:
        xy = q.pop()

        count += 1
        if count > groupMaxCount:
            groupMaxCount = count

        x = xy[0]
        y = xy[1]
        for i in range(4):
            nx = x+x_pos[i]
            ny = y+y_pos[i]
            if 0 <= nx and nx < size_m and 0 <= ny and ny < size_n:
                if d[nx][ny] == 0 and relation[nx][ny] != 0 and vlaue == relation[nx][ny]:
                    q.push([nx, ny])
                    d[nx][ny] = cnt

groupNum = 0
for i in range(size_m):
    for j in range(size_n):
        if d[i][j] == 0 and relation[i][j] != 0:
            groupNum += 1
            dfs(i, j, relation[i][j], groupNum)

for i in d:
    print (i)

print(groupNum, groupMaxCount)



