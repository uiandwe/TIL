# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        left_max, right_max = height[l], height[r]
        volume = 0

        while l < r:
            left_max, right_max = max(height[l], left_max), max(height[r], right_max)

            if left_max <= right_max:
                volume += left_max - height[l]
                l += 1

            else:
                volume += right_max - height[r]
                r -= 1

        return volume


    def trap1(self, height: List[int]) -> int:
        s = []
        volume = 0
        for i in range(len(height)):
            while s and height[i] > height[s[-1]]:
                t = s.pop()
                if not len(s):
                    break

                distance = i - s[-1] - 1
                waters = min(height[i], height[s[-1]]) - height[t]
                volume += distance * waters
            s.append(i)

        return volume



solution = Solution()
print(solution.trap1([0,1,0,2,1,0,1,3,2,1,2,1]))
