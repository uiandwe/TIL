# -*- coding: utf-8 -*-

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        c = [1]
        for i in range(1, len(s)):
            if s[i - 1] != s[i]:
                c.append(1)
            else:
                c[-1] += 1

        print(c)
        req = 0
        for i in range(len(c) - 1):
            req += min(c[i], c[i + 1])
        return req


s = Solution()
assert s.countBinarySubstrings("00110011") == 6
assert s.countBinarySubstrings("10101") == 4
