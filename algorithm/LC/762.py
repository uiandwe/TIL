# -*- coding: utf-8 -*-
from functools import lru_cache


class Solution:
    def countPrimeSetBits(self, L: int, R: int):
        ret = 0
        for i in range(L, R+1):
            if self.is_prime("{0:b}".format(i).count("1")):
                ret += 1
        return ret


    @lru_cache(maxsize=256)
    def is_prime(self, n: int):
        if n < 2:
            return False

        for i in range(2, n):
            if n % i is 0:
                return False
        return True



s = Solution()
assert s.countPrimeSetBits(6, 10) == 4
assert s.countPrimeSetBits(10, 15) == 5
