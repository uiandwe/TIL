# -*- coding: utf-8 -*-
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length = start = 0

        for index, value in enumerate(s):
            if value in used and start <= used[value]:
                start = used[value] + 1
            else:
                max_length = max(max_length, index - start + 1)

            used[value] = index
        return max_length



s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("pwwkew"))
