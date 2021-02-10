# -*- coding: utf-8 -*-
from typing import *
from collections import defaultdict

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        self.d = defaultdict(list)

        def split_path(s):
            file_path, *files = s.split(" ")

            for f in files:
                start, end = f.index("("), f.index(")")
                self.d[f[start+1:end]].append(file_path+"/"+f[:start])

        for p in paths:
            split_path(p)

        ret = [value for _, value in self.d.items() if len(value) > 1]
        print(ret)
        return ret

s = Solution()
s.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"])
