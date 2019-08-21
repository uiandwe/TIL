# -*- coding: utf-8 -*-
from operator import itemgetter

def solution(genres, plays):
    answer = []
    dict = {}
    for i, (a, b) in enumerate(zip(genres, plays)):
        if a in dict.keys():
            dict[a][0] = dict[a][0] + b
            dict[a][1].append([i, b])
            dict[a][1] = sorted(dict[a][1], key=itemgetter(1), reverse=True)
        else:
            dict[a] = [b, [[i, b]]]

    sort_dict = sorted(dict, key=lambda k: dict[k], reverse=True)
    for val in sort_dict:
        for a in dict[val][1][0:2]:
            answer.append(a[0])
    return answer


def test_solution():
    assert solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]) == [4, 1, 3, 0]


solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])

