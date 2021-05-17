# -*- coding: utf-8 -*-
from collections import defaultdict
from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        g = defaultdict(list)
        for i, l in enumerate(graph):
            for node in l:
                g[i].append(node)

        stack = []
        result = []

        def dfs(s, e):
            stack.append(s)

            if s == e:
                result.append([i for i in stack])
                return

            for i in g[s]:
                if i not in stack:
                    dfs(i, e)
                    stack.pop()

        dfs(0, len(graph)-1)

        return result



s = Solution()
assert s.allPathsSourceTarget([[1,2],[3],[3],[]]) == [[0,1,3],[0,2,3]]
assert s.allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]) == [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
assert s.allPathsSourceTarget([[1],[]]) == [[0,1]]
assert s.allPathsSourceTarget([[1,2,3],[2],[3],[]]) == [[0,1,2,3],[0,2,3],[0,3]]
assert s.allPathsSourceTarget([[1,3],[2],[3],[]]) == [[0,1,2,3],[0,3]]
