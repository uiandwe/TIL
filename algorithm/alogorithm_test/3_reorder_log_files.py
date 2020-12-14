# -*- coding: utf-8 -*-
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        l, d = [], []
        for log in logs:
            if log.split()[1].isdigit():
                d.append(log)
            else:
                l.append(log)

        l.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return l + d
