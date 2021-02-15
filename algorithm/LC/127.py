from typing import *
from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        self.ret_depth = float('inf')
        if endWord not in wordList:
            return 0

        L = len(beginWord)
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                all_combo_dict[word[:i] + "*" + word[i + 1:]].append(word)

        queue = deque([(beginWord, 1)])
        visited = set()
        visited.add(beginWord)

        while queue:
            current_word, level = queue.popleft()
            for i in range(L):
                intermediate_word = current_word[:i] + "*" + current_word[i + 1:]
                for word in all_combo_dict[intermediate_word]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited.add(word)
                        queue.append((word, level + 1))
        return 0



s = Solution()
assert s.ladderLength(beginWord = "hit", endWord = "cog", wordList = [ "hot", "dot", "dog", "lot", "log", "cog"]) == 5
assert s.ladderLength(beginWord = "hit", endWord = "cog", wordList = [ "hot", "dot", "dog", "lot", "log"]) == 0
assert s.ladderLength("hot", "dog", ["hot","dog"]) == 0
assert s.ladderLength("leet", "code", ["lest","leet","lose","code","lode","robe","lost"]) == 6

