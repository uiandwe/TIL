# -*- coding: utf-8 -*-
from typing import *
from collections import Counter, defaultdict

class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        if len(votes) == 1:
            return votes[0]

        ranks = defaultdict(lambda: [0] * len(votes[0]))

        for i in votes:
            for idx, l in enumerate(i):
                ranks[l][idx] -= 1

        srt = dict(sorted(ranks.items(), key=lambda x: (x[1], x[0])))

        return ''.join(srt.keys())


s = Solution()
assert s.rankTeams([ "ABC", "ACB", "ABC", "ACB", "ACB"]) == "ACB"
assert s.rankTeams([ "BCA", "CAB", "CBA", "ABC", "ACB", "BAC"]) == "ABC"
assert s.rankTeams(["WXYZ", "XYZW"]) == "XWYZ"
