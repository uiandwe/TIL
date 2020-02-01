
def solution(array, k):
    dict = {}
    for str in array:
        if str in dict:
            dict[str] += 1
        else:
            dict[str] = 1

    temp = sorted(dict, key=dict.get, reverse=True)[:k]
    print(temp)



solution(["i", "love", "leetcode", "i", "love", "coding"], 2)
solution(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4)


# -*- coding: utf-8 -*-
from collections import Counter
from operator import itemgetter

class Solution:
    def topKFrequent(self, words, k: int):

        c = Counter(words)

        count_array = list(c.items())

        count_array.sort(key=itemgetter(0))
        count_array.sort(key=itemgetter(1), reverse=True)

        ret_arr = []
        for i in range(k):
            ret_arr.append(count_array[i][0])

        return ret_arr

s = Solution()
assert s.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2) == ["i", "love"]
assert s.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4) == ["the", "is", "sunny", "day"]
