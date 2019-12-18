# -*- coding: utf-8 -*-
"""
Given an array of numbers, find the length of the longest increasing subsequence in the array.

The subsequence does not necessarily have to be contiguous.

For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15],

the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15.


"""
cache = None


def get_subseq(arr, start):
    if start == len(arr):
        return 0

    current = arr[start]
    max_inc = 1
    for index in range(start + 1, len(arr)):
        if arr[index] >= current:
            if index in cache:
                count = cache[index]
            else:
                count = get_subseq(arr, index) + 1
                cache[index] = count

            max_inc = max(count, max_inc)

    return max_inc


def get_subseq_helper(arr):
    global cache
    cache = dict()
    return get_subseq(arr, 0)


assert get_subseq_helper([]) == 0
assert get_subseq_helper([0, 1]) == 2
assert get_subseq_helper([0, 2, 1]) == 2
assert get_subseq_helper([0, 1, 2]) == 3
assert get_subseq_helper([2, 1, 0]) == 1
assert get_subseq_helper(
    [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]) == 6



maximum = 0

def _lis(arr, n):
    global maximum

    if n == 0:
        return 0

    if n == 1:
        return 1

    maxEndingHere = 1

    for i in range(1, n):
        res = _lis(arr, i)
        if arr[i-1] < arr[n-1] and res+1 > maxEndingHere:
            maxEndingHere = res + 1

    maximum = max(maximum, maxEndingHere)

    return maxEndingHere


def lis(arr):
    global maximum
    n = len(arr)

    if n == 0:
        return 0

    maximum = 1

    _lis(arr, n)

    return maximum

assert lis([]) == 0
assert lis([0, 1]) == 2
assert lis([0, 2, 1]) == 2
assert lis([0, 1, 2]) == 3
assert lis([2, 1, 0]) == 1
assert lis([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]) == 6
