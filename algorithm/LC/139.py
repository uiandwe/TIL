# -*- coding: utf-8 -*-
from typing import *
from collections import defaultdict, deque
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        n = len(s)
        dp = [False for _ in range(n+1)]

        dp[0] = True
        for i in range(n+1):
            # 1
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
            # 2
            # for word in wordDict:
            #     if dp[i-len(word)] and s[:i].endswith(word):
            #         dp[i] = True

        return dp[-1]





s = Solution()
assert s.wordBreak(s = "leetcode", wordDict = ["leet", "code", "lee"]) is True
assert s.wordBreak(s = "applepenapple", wordDict = ["apple", "pen"]) is True
assert s.wordBreak(s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]) is False
assert s.wordBreak(s = "aaaaaaaaaab", wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]) is False
