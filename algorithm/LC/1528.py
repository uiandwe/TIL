# -*- coding: utf-8 -*-
from typing import *
import collections
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        d = []
        for a, b in zip(s, indices):
            d.append((a, b))

        d.sort(key=lambda x: x[1])
        return ''.join(list(map(lambda x: x[0], d)))

s = Solution()
s.restoreString("codeleet", [4,5,6,7,0,2,1,3])

