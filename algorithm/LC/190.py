# -*- coding: utf-8 -*-
class Solution:
    def reverseBits(self, n: int) -> int:
        ret, p = 0, 31
        while n:
            ret += (n & 1) << p
            n = n >> 1
            p -= 1

        return ret
