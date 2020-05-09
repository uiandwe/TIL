# -*- coding: utf-8 -*-
class Solution:
    def maxArea(self, height):
        max_val = float('-inf')
        left = 0
        right = len(height)-1

        while left < right:
            hl, hr = height[left], height[right]
            max_val = max(max_val, abs(left - right) * min(hl, hr))
            if hl < hr:
                left += 1
            else:
                right -= 1

        return max_val



s = Solution()
s.maxArea([1,8,6,2,5,4,8,3,7])
