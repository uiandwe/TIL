# -*- coding: utf-8 -*-
class Solution:
    def convertToTitle(self, n: int) -> str:
        a = []
        while n > 0:
            n -= 1
            a.append(chr(65+n%26))
            n = n//26

        return ''.join(a[::-1])

s = Solution()
assert s.convertToTitle(1) == "A"
assert s.convertToTitle(26) == "Z"
assert s.convertToTitle(28) == "AB"
assert s.convertToTitle(27) == "AA"
assert s.convertToTitle(51) == "AY"
assert s.convertToTitle(52) == "AZ"
assert s.convertToTitle(701) == "ZY"
