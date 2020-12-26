# -*- coding: utf-8 -*-
import collections
class Solution:
    def findItinerary(self, tickets):
        graph = collections.defaultdict(list)

        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)

        route = []

        stack = ['JFK']

        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop(0))
            route.append(stack.pop())

        return route[::-1]


s = Solution()
print(s.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
