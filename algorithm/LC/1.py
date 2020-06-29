# -*- coding: utf-8 -*-
class Solution:
    def twoSum(self, nums, target: int):
        d = {}
        for idx, val in enumerate(nums):
            if target - val in d.keys():
                return [d[target - val], idx]
            else:
                d[val] = idx


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
