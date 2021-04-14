# -*- coding: utf-8 -*-


from collections import defaultdict


def dfs(vertex, word):
    while graph[vertex]:
        next_vertex, next_word = graph[vertex].pop()
        dfs(next_vertex, next_word)
    answer.append(word)

T = int(input())

for _ in range(T):
    N = int(input())
    words = {}
    graph = defaultdict(list)
    in_edge = defaultdict(int)
    out_edge = defaultdict(int)
    visited = {}

    for alpha in 'abcdefghijklmnopqrstuvwxyz':
        graph[alpha] = []
        in_edge[alpha] = 0
        out_edge[alpha] = 0

    for _ in range(N):
        word = input()
        graph[word[0]].append((word[-1], word))
        in_edge[word[-1]] += 1
        out_edge[word[0]] += 1

    answer = []

    candidates = []
    for alpha in 'abcdefghijklmnopqrstuvwxyz':
        if in_edge[alpha] != out_edge[alpha]:
            candidates.append(alpha)
    # 오일러 트레일

    if len(candidates) == 2:
        start = None
        end = None

        for alpha in candidates:
            # 시작 엣지는 out 이 in보다 하나더 많아야 한다.
            if in_edge[alpha] + 1 == out_edge[alpha]:
                start = alpha
            if in_edge[alpha] == out_edge[alpha] + 1:
                end = alpha

        if start and end:
            dfs(start, "")
    elif len(candidates) == 0:
        for alpha in 'abcdefghijklmnopqrstuvwxyz':
            if in_edge[alpha] is not 0:
                dfs(alpha, "")
                break
    if answer:
        print(" ".join(reversed(answer)).strip())
    else:
        print("IMPOSSIBLE")



"""
3
4
dog
god
dragon
need
3
aa
ab
bb
2
ab
cd



need dog god dragon
aa ab bb
IMPOSSIBLE

"""
