# -*- coding: utf-8 -*-
from typing import *
from collections import Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = Counter(tasks)

        lst = sorted(d.values(), reverse=True)
        max_nubmer = lst[0]

        i = 0
        counter = 0
        while i < len(lst) and lst[i] == max_nubmer:
            counter += 1
            i += 1

        ret = (max_nubmer - 1) * (n + 1) + counter
        return max(ret, len(tasks))

        # 2
        """
        d = Counter(tasks)

        result = 0
        while True:
            sub_count = 0
            for task, _ in d.most_common(n + 1):
                sub_count += 1
                result += 1

                d.subtract(task)
                d += Counter()

            if not d:
                break

            result += n - sub_count + 1

        return result
        """

        # 3
        # if n == 0:
        #     return len(tasks)
        #
        # c = Counter(tasks)
        # hq = []
        # for key, value in c.items():
        #     heapq.heappush(hq, (-value, key))
        #
        # ret = []
        # while hq:
        #     task_temp = []
        #     for i in range(n + 1):
        #         if not hq:
        #             ret.append("idle")
        #             continue
        #
        #         v, k = heapq.heappop(hq)
        #         ret.append(k)
        #         task_temp.append((v, k))
        #
        #     for t in task_temp:
        #         if t[0] + 1 != 0:
        #             heapq.heappush(hq, (t[0] + 1, t[1]))
        #
        # while ret:
        #     if ret[-1] == 'idle':
        #         ret.pop()
        #     else:
        #         break
        # return len(ret)




s = Solution()
assert s.leastInterval(tasks = ["A","A","A","B","B","B"], n = 2) == 8
assert s.leastInterval(tasks = ["A","A","A","B","B","B"], n = 0) == 6
assert s.leastInterval(tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2) == 16

