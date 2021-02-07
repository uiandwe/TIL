# -*- coding: utf-8 -*-
class Solution:
    def toHex(self, num: int) -> str:
        d = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

        if num < 0:
            num = pow(2, 32) + num
        ret = []
        while num >= 16:
            ret.append(d[num % 16])
            num = num >> 4
        ret.append(d[num])

        return ''.join(ret[::-1])


s = Solution()
assert s.toHex(26) == "1a"
assert s.toHex(0) == "0"
assert s.toHex(-1) == "ffffffff"
