import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import acmicpc_1932
import json

def test_solve():
    with open('./1932_1.json') as f:
        data = json.load(f)

    assert 30 == acmicpc_1932.solution(data["data"])

    with open('./1932_2.json') as f:
        data = json.load(f)

    assert 15 == acmicpc_1932.solution(data["data"])
