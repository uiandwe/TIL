# -*- coding: utf-8 -*-
from collections import defaultdict, Counter
from queue import PriorityQueue
import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        d = defaultdict(int)
        q = PriorityQueue()

        paragraph = re.sub(r'[^\w]', ' ', paragraph)

        d = Counter(paragraph.lower().split(" "))
        del d['']

        for b in banned:
            if b in d:
                del d[b]

        return d.most_common(1)[0][0]

