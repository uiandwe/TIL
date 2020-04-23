from collections import Counter

class Solution:
    def countElements(self, arr):
        arr = sorted(arr)
        answer = 0

        d = Counter(arr)

        for key in d.keys():
            if key+1 in d:
                answer += d[key]

        return answer

s = Solution()
assert s.countElements([1,3,2,3,5,0]) == 3
assert s.countElements([1,1,2,2]) == 2