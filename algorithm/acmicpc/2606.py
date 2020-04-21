# -*- coding: utf-8 -*-
"""
4
4
4 3
1 3
2 4
2 3
"""

def dfs(d, visite, now, group):
    visite[now] = group
    n = len(d)

    now_path = d[now]
    for i in range(1, n):
        if now != i and now_path[i] == 1 and visite[i] == 0:
            dfs(d, visite, i, group)


def solution(n, nodes):
    visite = [0 for x in range(n+1)]
    d = [[0 for x in range(n+1)] for y in range(n+1)]

    for node in nodes:
        s = node[0]
        e = node[1]

        d[s][e] = 1
        d[e][s] = 1

    group = 1
    for i in range(1, n+1):
        if visite[i] == 0:
            dfs(d, visite, i, group)
            group += 1

    answer = 0
    virus_num = visite[1]
    for i, val in enumerate(visite):
        if i != 1 and val == virus_num:
            answer += 1

    print(answer)


if __name__ == '__main__':
    n = int(input())
    c = int(input())
    nodes = []
    for i in range(c):
        node = input()
        nn = node.split(" ")
        nodes.append([int(nn[0]), int(nn[1])])

    solution(n, nodes)
