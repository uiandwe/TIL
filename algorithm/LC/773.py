# -*- coding: utf-8 -*-
from typing import *
from collections import deque

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        visit = set()
        moves = {0:(1, 3), 1:(0, 2, 4), 2:(1, 5), 3:(0, 4), 4:(1, 3, 5), 5:(2, 4)}
        state = "".join([str(i) for i in board[0]+board[1]])
        index = state.index("0")

        queue = deque([(index, state, 0)])

        while queue:
            cur, state, steps = queue.popleft()
            if state == '123450':
                return steps
            elif state in visit:
                continue
            else:
                visit.add(state)
                for i in moves[cur]:
                    temp = list(state)
                    temp[cur], temp[i] = temp[i], temp[cur]
                    temp = ''.join(temp)
                    queue.append((i, temp, steps+1))
        return -1



s = Solution()
assert s.slidingPuzzle([[1, 2, 3], [4, 0, 5]]) == 1
assert s.slidingPuzzle([[1,2,3], [5,4,0]]) == -1
assert s.slidingPuzzle([[4,1,2], [5,0,3]]) == 5
assert s.slidingPuzzle([[3,2,4], [1,5,0]]) == 14
