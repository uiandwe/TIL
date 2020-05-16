# -*- coding: utf-8 -*-
class Solution:
    def find_search(self, nums, target, t):
        l = 0
        h = len(nums)
        while l < h:
            mid = (l + h) // 2
            temp = nums[mid]
            if temp > target or (temp == target and t):
                h = mid
            else:
                l = mid + 1
        return l

    def searchRange(self, nums, target: int):
        if len(nums) <= 0:
            return [-1, -1]

        left = self.find_search(nums, target, True)

        if left >= len(nums) or nums[left] != target:
            return [-1, -1]

        right = self.find_search(nums, target, False) -1

        return [left, right]


s = Solution()
print(s.searchRange([5,7,7,8,8,10], 8))
print(s.searchRange([5,7,7,8,8,10], 6))
print(s.searchRange([1], 1))
print(s.searchRange([2, 2], 2))
print(s.searchRange([1, 1, 2], 1))
print(s.searchRange([], 0))
print(s.searchRange([2, 2], 3))
