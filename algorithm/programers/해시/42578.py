# -*- coding: utf-8 -*-
from collections import Counter

"""
    예를들어 머리:3, 얼굴:2, 옷:1 이라면 총 가능한 개수는
    (3+1) * (2+1) * (1+1) -1 = 13
    +1씩을 더한 것은 착용하지 않은 경우가 추가 되기 때문이고 마지막으로 -1을 한것은 모든 부위를 입지 않은 경우
"""
def solution(clothes):
    answer = 1
    c = Counter([x[1] for x in clothes])
    for v in c.values():
        answer *= v+1 # 착용하지 않는 경우의 수를 더함
    return answer-1 # 아무것도 않입는 경우의 수를 뺌


def test_solution():
    assert solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]) == 5
    assert solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]) == 3

