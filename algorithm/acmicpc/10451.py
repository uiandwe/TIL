# -*- coding: utf-8 -*-
from typing import List


def dfs(a: List, v: List, index: int, g: int):
    v[index] = g
    next_a = a[index]-1

    if v[next_a] == 0:
        dfs(a, v, next_a, g)

    return


def solution(array: List):
    visite = [0 for x in array]

    group = 1
    for i, val in enumerate(array):
        if visite[i] == 0:
            dfs(array, visite, array[i]-1, group)
            group += 1

    print(visite)
    print(group-1)


solution([3, 2, 7, 8, 1, 4, 5, 6])
solution([2, 1, 3, 4, 5, 6, 7, 9, 10, 8])
