# -*- coding: utf-8 -*-
class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''

        def long(start, end):
            while start >= 0 and end <= len(s) and s[start] == s[end-1]:
                start -= 1
                end += 1
            return s[start+1:end-1]

        for i in range(len(s)-1):
            result = max(result, long(i, i+1), long(i, i+2), key=len)

        return result


s = Solution()
# assert s.longestPalindrome("babad") == "bab"
assert s.longestPalindrome("abb") == "bb"
