# -*- coding: utf-8 -*-
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set_temp = set(s)
        if len(set_temp) == 0:
            return 0
        elif len(set_temp) == 1:
            return 1

        i = 0
        j = 0
        d = {}
        ans = 0
        while j < len(s):
            if s[j] not in d or i > d[s[j]]:
                ans = max(ans, (j - i + 1))
                d[s[j]] = j
            else:
                i = d[s[j]] + 1
                ans = max(ans, (j - i + 1))
                j -= 1
            # print(ans)
            j += 1
        # print(ans)
        return ans

s = Solution()
# s.lengthOfLongestSubstring("bbbbbb")
s.lengthOfLongestSubstring("abcabcbb")
# s.lengthOfLongestSubstring("pwwkew")
