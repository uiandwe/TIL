# -*- coding: utf-8 -*-
from itertools import permutations

def get_permutation(array):
    premutations = []
    for p in permutations(array):
        premutations.append(list(p))
    return premutations


assert get_permutation([1, 2, 3]) == [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
