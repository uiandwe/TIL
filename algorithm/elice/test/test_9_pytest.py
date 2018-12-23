import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import elice9


def test_q():
    assert "35052" == elice9.changeNToM(5000, 6)
    assert "2A88" == elice9.changeNToM(5000, 12)

