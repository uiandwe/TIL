# -*- coding: utf-8 -*-
def solution(X, A):
    check = [False] * X
    check_sum = 0

    for idx, val in enumerate(A):
        if check[val-1] is False:
            check[val-1] = True
            check_sum += 1
            if X == check_sum:
                return idx
    return -1
