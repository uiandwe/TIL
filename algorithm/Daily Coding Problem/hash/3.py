# -*- coding: utf-8 -*-
"""
Given an array of elements, return the length of the longest subarray where all its elements are distinct.

For example, given the array [5, 1, 3, 5, 2, 3, 4, 1], return 5 as the longest subarray of distinct elements is [5, 2, 3, 4, 1].
"""

def solution(arr):
    d = {}
    for i, v in enumerate(arr):
        if v in d.keys():
            return arr[i:]
        else:
            d[v] = i
    return arr


assert solution([5, 1, 3, 5, 2, 3, 4, 1]) == [5, 2, 3, 4, 1]
