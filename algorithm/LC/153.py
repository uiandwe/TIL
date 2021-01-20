# -*- coding: utf-8 -*-
from typing import *
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1

        while left < right:
            mid = left + (right - left) // 2

            if nums[right] < nums[left]:
                if nums[mid] < nums[right]:
                    right = mid
                else:
                    left = mid+1
            else:
                if nums[mid] < nums[right]:
                    right = mid-1
                else:
                    left = mid
        return nums[left]


s = Solution()
assert s.findMin([3, 4, 5, 1, 2]) == 1
assert s.findMin([4,5,6,7,0,1,2]) == 0
assert s.findMin([11,13,15,17]) == 11
