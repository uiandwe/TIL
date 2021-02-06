# -*- coding: utf-8 -*-
import math


class Solution:
    def isHappy(self, n: int) -> bool:
        d = set()
        while True:
            n = self.cal(n)
            if n in d:
                return False
            elif n == 1:
                return True
            d.add(n)

    def cal(self, n):
        ret = 0
        while n >= 10:
            ret += pow((n % 10), 2)
            n = n // 10
        ret += pow(n, 2)
        return ret


s = Solution()
assert s.isHappy(19) is True
assert s.isHappy(1) is True
assert s.isHappy(2) is False
assert s.isHappy(7) is True
