# -*- coding: utf-8 -*-
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle or needle == "":
            return 0

        if haystack and needle:
            try:
                return haystack.index(needle)
            except Exception:
                return -1
        return -1


if __name__ == '__main__':
    s = Solution()
    s.strStr("aaaa", "bba")
