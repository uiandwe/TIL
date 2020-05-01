# -*- coding: utf-8 -*-
import itertools

class Solution:
    def subsets(self, nums):

        arr = [[]]
        for i in range(1, len(nums) + 1):
            for values in list(itertools.combinations(nums, i)):
                arr.append(list(values))

        return arr


s = Solution()
s.subsets([1, 2, 3])
