# -*- coding: utf-8 -*-
class Solution:
    def twoSum(self, nums, target: int):
        d = {nums[0]: 0}
        for n in range(1, len(nums)):
            if target - nums[n] in d.keys():
                return d[target-nums[n]], n
            else:
                d[nums[n]] = n

s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
