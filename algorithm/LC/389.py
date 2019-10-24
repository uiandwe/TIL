# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/find-the-difference/submissions/
"""
import collections

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        lst = collections.Counter(s)

        for char in t:
            lst[char] -= 1
            if lst[char] <= -1:
                return char



