# -*- coding: utf-8 -*-
class Solution:
    def subarraySum(self, nums, k: int):
        d = {0:1}
        answer = 0
        s = 0

        for num in nums:
            s += num
            if s-k in d:
                answer += d[s-k]
            if s in d:
                d[s] += 1
            else:
                d[s] = 1
        print(d)
        print(answer)
        return answer


s = Solution()
s.subarraySum([1, 1, 1], 2)
# s.subarraySum([1], 0)
# s.subarraySum([1, 2, 3], 3)
# s.subarraySum([-1, -1, 1], 0)
