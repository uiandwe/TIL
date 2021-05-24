# -*- coding: utf-8 -*-
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        d = ["" for _ in range(n+1)]
        d[0] = "0"

        def invert(t: str):
            return (format(int(t, 2) ^ int(2 ** (len(t)) - 1), 'b'))

        for i in range(1, n+1):
            temp1 = d[i-1]
            d[i] = temp1 + "1" + invert(temp1)[::-1]

        return d[n][k-1]


s = Solution()
s.findKthBit(3, 1)
