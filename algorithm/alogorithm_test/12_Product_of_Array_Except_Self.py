# -*- coding: utf-8 -*-
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        result = []

        for i in range(len(nums)):
            result.append(p)
            p = p * nums[i]

        p = 1
        for i in range(len(nums) - 1, 0, -1):
            result[i - 1] = result[i - 1] * nums[i] * p
            p *= nums[i]

        return result
