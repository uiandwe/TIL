# -*- coding: utf-8 -*-
"""
Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137,

since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

Do this in O(N) time.

"""

def get_max_sum(n):
    d = [0 for x in n]
    p = n[0] if n[0] > 0 else 0
    d[0] = p

    for i in range(1, len(n)):
        if p + n[i] > 0:
            p += n[i]
        else:
            p = 0

        d[i] = p

    print(d)
    return max(d)



assert get_max_sum([34, -50, 42, 14, -5, 86]) == 137
assert get_max_sum([-5, -1, -8, -9]) == 0
