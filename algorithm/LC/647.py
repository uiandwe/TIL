# -*- coding: utf-8 -*-
class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0

        def long(start, end):
            ans = 0
            while start >= 0 and end <= len(s) and s[start] == s[end - 1]:
                start -= 1
                end += 1
                ans += 1
            return ans

        for i in range(len(s)):
            result += long(i, i+1)
            result += long(i, i+2)

        return result


s = Solution()
print(s.countSubstrings("aaa"))
print(s.countSubstrings("abc"))
