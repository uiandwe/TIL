# -*- coding: utf-8 -*-
from typing import *


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        length = float('inf')
        l = 0
        r = 0
        while l < len(nums) and r < len(nums):
            result = sum(nums[l:r+1])
            print(result)
            if result >= s:
                length = min(length, (r-l)+1)
                l += 1
            else:
                r += 1

        if length > len(nums):
            return 0
        return length

    #     n, res = len(nums), len(nums) + 1
    #     sums = [0] * (n + 1)
    #     for i in range(1, n + 1):
    #         sums[i] = sums[i - 1] + nums[i - 1]
    #
    #     for left in range(0, n + 1):
    #         right = self.binarySearch(left + 1, n, sums[left] + s, sums)
    #         print("right", right)
    #     print(sums)
    #
    # def binarySearch(self, left, right, val, sums):
    #     print(left, right, val, sums)
    #     while left <= right:
    #         mid = left + (right - left) // 2
    #         if sums[mid] < val:
    #             left = mid + 1
    #         else:
    #             right = mid - 1
    #     return left



s = Solution()
assert s.minSubArrayLen(7, [2,3,1,2,4,3]) == 2
# assert s.minSubArrayLen(6, [10, 2, 3]) == 1
# assert s.minSubArrayLen(3, [1, 1]) == 0
