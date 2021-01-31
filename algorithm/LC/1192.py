# -*- coding: utf-8 -*-
from typing import *
from collections import defaultdict

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

        dic = defaultdict(list)
        for c in connections:
            u, v = c
            dic[u].append(v)
            dic[v].append(u)

        timer = 0

        depth, lowest, parent, visited = [float("inf")] * n, [float("inf")] * n, [float("inf")] * n, [False] * n
        res = []

        def find(u):

            if visited[u]:
                return

            nonlocal timer

            visited[u] = True
            depth[u], lowest[u] = timer, timer
            timer += 1

            for v in dic[u]:

                if not visited[v]:
                    parent[v] = u
                    find(v)
                    if lowest[v] > depth[u]:
                        res.append([u, v])

                if parent[u] != v:
                    lowest[u] = min(lowest[u], lowest[v])

        for i in range(n):
            find(i)
        print(depth, lowest, parent, visited)
        return res


s = Solution()
assert s.criticalConnections(4, [[0,1],[1,2],[2,0],[1,3]]) == [[1, 3]]
assert s.criticalConnections(6, [[0,1],[1,2],[2,0],[3,4],[4,5],[5,3]]) == [[1, 3]]
assert s.criticalConnections(6, [[0,1],[1,2],[2,0],[1,3],[3,4],[4,5],[5,3]]) == [[1, 3]]
