# -*- coding: utf-8 -*-
import collections
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    a = collections.defaultdict(list)

    for word in strs:
        a[''.join(sorted(word))].append(word)

    return a.values()
