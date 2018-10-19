# -*- coding: utf8 -*-
'''
입력1
1 3 1
2 2 1
3 7 1
4 8 1
5 1 1
6 4 1
7 5 1
8 6 1

입력 2

1 2 1
2 1 1
3 3 1
4 4 1
5 5 1
6 6 1
7 7 1
8 9 1
9 10 1
10 8 1
'''

a = []
check = []
cycle = []


for i in range(10+1):
    a.append([])
    check.append(0)


for i in range(10):
    str = raw_input()
    str = str.split(' ')
    node = str[0]
    v = str[1]
    w = str[2]

    vector = [int(v), int(w)]
    a[int(node)].append(vector)


for i in a:
    print i


def dfs(start, node):
    check[node] = 1
    cycle.append(start)
    for i in range(len(a[node])):
        y = a[node][i][0]
        if check[y] == 0:
            return dfs(node, y)
        elif check[y] == 1 and node == y: #자기 자신일 경우
            print "자기자신", node
            return 0
        elif check[y] == 1 and y in cycle: #사이클일 경우
            cycle.append(node)
            print "사이클", cycle
            return 0


for i in range(1, len(a)):
    cycle = []
    start = i
    node = i
    if check[i] == 0:
        dfs(start, node)
