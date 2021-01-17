# -*- coding: utf-8 -*-
from math import sqrt, log
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        return 3 ** round(log(n, 3)) == n


s = Solution()
assert s.isPowerOfThree(27) is True
assert s.isPowerOfThree(7) is False
assert s.isPowerOfThree(9) is True
