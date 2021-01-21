# -*- coding: utf-8 -*-
from typing import *
class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target or nums[right] == target or nums[left] == target:
                return True

            if nums[left] < nums[right]:
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            elif nums[left] >= nums[right]:
                right -= 1

        return False


s = Solution()
assert s.search(nums = [2,5,6,0,0,1,2], target = 0) is True
assert s.search(nums = [2,5,6,0,0,1,2], target = 3) is False
assert s.search(nums = [1,0,1,1,1], target = 0) is True
assert s.search(nums = [1], target = 0) is False
assert s.search(nums = [1], target = 1) is True
assert s.search(nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1], target = 2) is True


