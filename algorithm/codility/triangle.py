# -*- coding: utf-8 -*-
def solution(array):
    array.sort()

    for i in range(len(array)-2):
        if array[i] + array[i+1] > array[i+2]:
            return 1

    return 0


assert solution([10, 2, 5, 1, 8, 20]) == 1
assert solution([10, 50, 5, 1]) == 0
