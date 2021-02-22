# -*- coding: utf-8 -*-
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        d = []
        for word in s:
            if word.strip() != "":
                d.append(word)
        print(d)
        return " ".join(d[::-1])


s = Solution()
assert s.reverseWords("a good   example") == "example good a"
assert s.reverseWords("  hello world  ") == "world hello"
