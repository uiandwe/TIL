# -*- coding: utf-8 -*-

import collections

class Solution:
    def characterReplacement(self, s: str, k: int):
        left = right = 0
        counts = collections.Counter()

        for right in range(1, len(s) + 1):
            counts[s[right - 1]] += 1
            max_char_n = counts.most_common(1)[0][1]


            if  right - left - max_char_n > k:
                counts[s[left]] -= 1
                left += 1
        return right - left


s = Solution()
s.characterReplacement(s = "ABAB", k = 2)
