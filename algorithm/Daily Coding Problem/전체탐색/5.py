# -*- coding: utf-8 -*-
"""
Given an array of integers where every integer occurs three times except for one integer, 
which only occurs once, find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.

"""
def getSingle(arr):
    ones = 0
    twos = 0
    n = len(arr)

    for i in range(n):
        twos = twos | (ones & arr[i])

        ones = ones ^ arr[i]

        common_bit_mask = ~(ones & twos)

        ones &= common_bit_mask

        twos &= common_bit_mask

    return ones

if __name__ == '__main__':
    print(getSingle([13, 1, 13, 13]))
    print(getSingle([13, 1, 13, 13, 2, 3, 2, 3, 2, 3]))
