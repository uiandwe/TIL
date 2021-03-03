# -*- coding: utf-8 -*-
from collections import defaultdict
class Solution:
    def possibleBipartition(self, N, dislikes) -> bool:
        graph = defaultdict(list)
        group_mapping = dict()
        visit = set()
        for (u, v) in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(i, g):
            if i in group_mapping and g != group_mapping[i]:
                return False
            group_mapping[i] = g
            if i not in visit:
                visit.add(i)
                for d in graph[i]:
                    if not dfs(d, not g):
                        return False
            return True

        for i in range(1, N + 1):
            if i in visit:
                continue
            if not dfs(i, True):
                return False

        return True


s = Solution()
assert s.possibleBipartition(N = 4, dislikes = [[1,2],[1,3],[2,4]]) is True
assert s.possibleBipartition( N = 3, dislikes = [[1,2],[1,3],[2,3]]) is False
assert s.possibleBipartition( N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]) is False




