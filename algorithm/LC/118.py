# -*- coding: utf-8 -*-
from typing import *


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []

        d = [[1]]

        for i in range(1, numRows):
            row = [1]
            for j in range(1, len(d[i-1])):
                row.append(d[i-1][j-1] + d[i-1][j])
            d.append(row + [1])

        return d


