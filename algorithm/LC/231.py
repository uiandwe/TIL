# -*- coding: utf-8 -*-
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False

        ret = False
        while n:
            temp = n & 1
            if ret and temp:
                return False

            if temp:
                ret = True
            n = n >> 1

        return True



s = Solution()
assert s.isPowerOfTwo(0) == False
assert s.isPowerOfTwo(16) == True
assert s.isPowerOfTwo(4) == True
assert s.isPowerOfTwo(3) == False
assert s.isPowerOfTwo(5) == False
