import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import acmicpc_1932

def test_solve():
    inputData = [
        [7],
        [3, 8],
        [8, 1, 0],
        [2, 7, 4, 4],
        [4, 5, 2, 6, 5]
    ]
    assert 30 == acmicpc_1932.solution(inputData)

    inputData = [
        [7],
        [3, 8]
    ]

    assert 15 == acmicpc_1932.solution(inputData)
