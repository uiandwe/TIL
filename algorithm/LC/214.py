# -*- coding: utf-8 -*-
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s
        for i in range(len(s)-1, -1, -1):
            if s[:i+1]==s[:i+1][::-1]:
                return s[i+1:][::-1]+s


s =Solution()

assert s.shortestPalindrome("aacecaaa") == "aaacecaaa"
assert s.shortestPalindrome("abcd") == "dcbabcd"
assert s.shortestPalindrome("abb") == "bbabb"
