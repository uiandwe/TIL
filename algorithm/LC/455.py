# -*- coding: utf-8 -*-
from typing import *
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()

        i, j = 0, 0
        while i < len(s) and j < len(g):
            if s[i] >= g[j]:
                j += 1
            i += 1
        return j

s = Solution()
assert s.findContentChildren(g = [1,2,3], s = [1,1]) == 1
assert s.findContentChildren(g = [1,2], s = [1,2,3]) == 2
