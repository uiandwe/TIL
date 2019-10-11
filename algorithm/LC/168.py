# -*- coding: utf-8 -*-
class Solution:
    def convertToTitle(self, n: int) -> str:
        str = ''
        if n < 27:
            return chr(64+n)

        while n > 0:
            tmp = (n - 1) % 26 + ord('A')
            n = (n - 1) // 26
            str = chr(tmp) + str
        return str



s = Solution()
assert s.convertToTitle(1) == "A"
assert s.convertToTitle(26) == "Z"
assert s.convertToTitle(28) == "AB"
assert s.convertToTitle(27) == "AA"
assert s.convertToTitle(51) == "AY"
assert s.convertToTitle(52) == "AZ"
assert s.convertToTitle(701) == "ZY"
