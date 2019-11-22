# -*- coding: utf-8 -*-
"""
Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137,

since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

Do this in O(N) time.

"""

def get_max_subarray(n):

    if not n or max(n) < 0:
        return 0

    current_p = n[0]
    overall_p = n[0]

    for val in n[1:]:
        current_p = max(val, current_p+val)
        overall_p = max(current_p, overall_p)

    return overall_p

assert get_max_subarray([34, -50, 42, 14, -5, 86]) == 137
assert get_max_subarray([-5, -1, -8, -9]) == 0
assert get_max_subarray([44, -5, 42, 14, -150, 86]) == 95
