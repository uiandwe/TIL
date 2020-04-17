# -*- coding: utf-8 -*-
from operator import itemgetter


def solution(genres, plays):
    answer = []
    play_total = {}
    dict = {}

    for i, (genre, count) in enumerate(zip(genres, plays)):
        # print(i, genre, count)
        if genre in dict.keys():
            play_total[genre] += count
            dict[genre].append((count, i))
        else:
            dict[genre] = [(count, i)]
            play_total[genre] = count

    top_play_list = sorted(play_total, key=lambda k: play_total[k], reverse=True)

    for genre in top_play_list:
        l = sorted(dict[genre], key=itemgetter(0), reverse=True)
        for idx, val in enumerate(l):
            if idx >= 2:
                break
            answer.append(val[1])

    return answer


assert solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]) == [4, 1, 3, 0]


solution(["classic", "pop", "classic", "classic", "pop"], [800, 600, 500, 500, 2500])

