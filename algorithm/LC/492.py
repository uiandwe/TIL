# -*- coding: utf-8 -*-
from typing import *
from math import sqrt

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        for i in range(int(sqrt(area)), 0, -1):
            if area % i == 0:
                return [area // i, i]


s = Solution()
assert s.constructRectangle(4) == [2, 2]
assert s.constructRectangle(37) == [37, 1]
assert s.constructRectangle(122122) == [427, 286]
assert s.constructRectangle(1) == [1, 1]


