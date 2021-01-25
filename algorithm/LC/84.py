# -*- coding: utf-8 -*-
from typing import *


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) <= 0:
            return 0

        d = []
        max_area = 0
        for i, h in enumerate(heights):
            start = i

            while d and d[-1][1] > h:
                index, height = d.pop()
                max_area = max(max_area, height * (i - index))
                start = index
            d.append((start, h))
        print(d)
        for i, h in d:
            max_area = max(max_area, h * (len(heights) - i))
        return max_area


s = Solution()
# assert s.largestRectangleArea([2,1,5,6,2,3]) == 10
# assert s.largestRectangleArea([2,4]) == 4
# assert s.largestRectangleArea([2,2]) == 4
assert s.largestRectangleArea([5,4,1,2]) == 8

