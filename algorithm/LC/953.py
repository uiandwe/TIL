# -*- coding: utf-8 -*-
from typing import *
from collections import defaultdict
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        # return words == sorted(words,key=lambda word:[order.index(c) for c in word])

        d = defaultdict(list)
        order_i = []
        for word in words:
            ch = word[0]
            order_i.append(order.index(ch))

            if ch in d.keys():
                for item in d[ch]:
                    for c1, c2 in zip(item, word):
                        if order.index(c1) > order.index(c2):
                            return False

                    if item != word and item.startswith(word):
                        return False

            d[ch].append(word)

        # print(order_i)

        for i in range(1, len(order_i)):
            if order_i[i-1] > order_i[i]:
                return False

        return True




s = Solution()
assert s.isAlienSorted(words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz") is True
assert s.isAlienSorted(words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz") is False
assert s.isAlienSorted( words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz") is False
assert s.isAlienSorted(["apap","app"], "abcdefghijklmnopqrstuvwxyz") is True
assert s.isAlienSorted(["hello","hello"], "abcdefghijklmnopqrstuvwxyz") is True

