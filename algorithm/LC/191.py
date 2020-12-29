# -*- coding: utf-8 -*-
class Solution:
    def hammingWeight(self, n: int) -> int:
        ret = 0
        while n:
            ret += 1 if (n & 1) > 0 else 0
            n = n >> 1
        return ret
