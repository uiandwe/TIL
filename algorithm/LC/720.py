# -*- coding: utf-8 -*-
from typing import *
from collections import defaultdict, Counter

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Solution:
    def longestWord(self, words: List[str]) -> str:
        # d = Counter(words)
        # ret = []
        #
        # for word in sorted(words, key=len, reverse=True):
        #     s = ""
        #     for c in word:
        #         s += c
        #         if s not in d.keys():
        #             break
        #
        #     if s == word:
        #         ret.append((word, len(word)))
        #
        # ret.sort(key=lambda x: (-x[1], x[0]))
        #
        # return ret[0][0]
        self.root = TrieNode()
        words = sorted(set(words), key=lambda word:(-len(word), word))

        for word in words:
            cur = self.root
            for letter in word:
                if letter not in cur.children:
                    cur.children[letter] = TrieNode()
                cur = cur.children[letter]

            cur.end = True

        for word in words:
            flag = True
            cur = self.root
            for letter in word:
                if cur.children[letter].end == False:
                    flag = False
                    break
                else:
                    cur = cur.children[letter]
            if flag:
                return word
        return ''




s = Solution()
assert s.longestWord(["a", "w","wo","wor","worl", "world"]) == "world"
assert s.longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"]) == "apple"

