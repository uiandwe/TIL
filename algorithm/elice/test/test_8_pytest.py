import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import elice8


def test_q():
    assert [1, 2, 3, 5] == elice8.q([1, 5, 2, 3])
    assert [2, 3, 4, 7, 9, 20, 100] == elice8.q([3, 4, 7, 2, 100, 9, 20])
    assert [] == elice8.q([])

