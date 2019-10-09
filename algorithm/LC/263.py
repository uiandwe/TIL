# -*- coding: utf-8 -*-
# https://leetcode.com/problems/ugly-number/submissions/

class Solution:
    def isUgly(self, num: int) -> bool:

        while num >= 1:

            if num % 2 == 0:
                num = num // 2
            elif num % 3 == 0:
                num = num // 3
            elif num % 5 == 0:
                num = num // 5
            elif num == 1:
                return True
            else:
                return False

        return False

s = Solution()
assert s.isUgly(6) is True
assert s.isUgly(8) is True
assert s.isUgly(14) is False
assert s.isUgly(10) is True
assert s.isUgly(-2147483648) is False


