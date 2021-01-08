# -*- coding: utf-8 -*-
from collections import defaultdict
class Solution:
    def arrangeWords(self, text: str) -> str:
        text = text.split()
        text.sort(key=len)
        return ' '.join(text).capitalize()

s = Solution()
assert s.arrangeWords(text = "Leetcode is cool") == "Is cool leetcode"
assert s.arrangeWords(text = "Keep calm and code on") == "On and keep calm code"
assert s.arrangeWords(text = "To be or not to be") == "To be or to be not"
