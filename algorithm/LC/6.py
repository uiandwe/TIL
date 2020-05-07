# -*- coding: utf-8 -*-
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        d = [[] for i in range(numRows)]

        index = 0
        revers = False
        for i, c in enumerate(s):
            d[index].append(c)
            if not revers:
                index += 1
            if not revers and index == numRows:
                revers = True
                index -= 1
            if revers:
                if index > 0:
                    index -= 1

                if index == 0:
                    revers = False

        answer = ''.join([''.join(temp_s) for temp_s in d])
        return answer

s = Solution()
s.convert("PAYPALISHIRING", 3)
s.convert("PAYPALISHIRING", 4)
s.convert("ABC", 1)
