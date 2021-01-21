# -*- coding: utf-8 -*-
from typing import *
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[left] <= nums[mid]:
                if nums[left] < nums[right]:
                    right = mid - 1
                else:
                    left += 1
            else:
                right -= 1
        return nums[left]


s = Solution()
assert s.findMin([1, 3, 5]) == 1
assert s.findMin([2, 2, 2, 2, 0, 1]) == 0
assert s.findMin([3, 5, 1]) == 1
assert s.findMin([10,1,10,10,10]) == 1

