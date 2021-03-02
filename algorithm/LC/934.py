# -*- coding: utf-8 -*-
from typing import *
from collections import defaultdict, deque


class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:

        self.n = len(A)
        self.m = len(A[0])
        q = deque()
        visit = defaultdict(int)

        def mark_island(y, x, mark_number):
            if 0 <= y < self.n and 0 <= x < self.m and A[y][x] == 1:
                q.append((y, x, 0))
                A[y][x] = mark_number
                mark_island(y + 1, x, mark_number)
                mark_island(y - 1, x, mark_number)
                mark_island(y, x + 1, mark_number)
                mark_island(y, x - 1, mark_number)

        def first_mark_island():
            for y in range(self.n):
                for x in range(self.m):
                    if A[y][x] == 1:
                        mark_island(y, x, -1)
                        return y, x
        # first = -1
        # second = 1
        start_y, start_x = first_mark_island()

        # for a in A:
        #     print(a)
        # print(q)
        # print(visit)

        q.append((start_y, start_x, 0))
        ret = float('inf')
        while q:
            node_y, node_x, step = q.popleft()
            if 0 <= node_y < self.n and 0 <= node_x < self.m and (node_y, node_x) not in visit.keys():
                visit[(node_y, node_x)] = 1
                if A[node_y][node_x] == 1:
                    ret = min(ret, step)

                q.append((node_y+1, node_x, step+1))
                q.append((node_y-1, node_x, step+1))
                q.append((node_y, node_x+1, step+1))
                q.append((node_y, node_x-1, step+1))
        # print(ret)

        return ret - 1



s = Solution()
assert s.shortestBridge([[0, 1, 0], [0, 0, 0], [0, 0, 1]]) == 2
assert s.shortestBridge([[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]) == 1
