import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import elice11


def test_solve():
    assert '3.0' == elice11.cal("1+2")
    assert '49.0' == elice11.cal("(2+5)*7/(3-2)")
    assert '20.0' == elice11.cal("4*(3+2)")
    assert '-1.0' == elice11.cal("1-2")
    assert '-5.0' == elice11.cal("(1-2)*5")
    assert '55.0' == elice11.cal("1+2+3+4+5+6+7+8+9+10")
    assert '1000000.0' == elice11.cal("100*100*100")
