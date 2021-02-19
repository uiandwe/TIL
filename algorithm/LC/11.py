# -*- coding: utf-8 -*-
class Solution:
    def maxArea(self, height):
        l = m = 0
        r = len(height) - 1

        while l < r:
            if height[l] > height[r]:
                m = max(height[r] * (r-l), m)
                r -= 1
            else:
                m = max(height[l] * (r-l), m)
                l += 1

        return m


s = Solution()
assert s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
assert s.maxArea([1, 1]) == 1
assert s.maxArea([2, 1]) == 1
