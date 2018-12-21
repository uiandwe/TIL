import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import elice7


def test_solve():
    assert 1 == elice7.solve(3)
    assert 1 == elice7.solve(5)
    assert 2 == elice7.solve(8)
    assert -1 == elice7.solve(4)
    assert 4 == elice7.solve(18)
