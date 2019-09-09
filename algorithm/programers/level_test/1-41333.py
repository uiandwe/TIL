# -*- coding: utf-8 -*-
def solution(s):
    operator = 1
    if s[0] in ["+", "-"]:
        if s[0] == "-":
            operator = -1
        s = s[1:]

    return int(s) * operator



def test_solution():
    assert solution("1234") == 1234
    assert solution("-1234") == -1234
    assert solution("+1234") == 1234
    assert solution("1") == 1
    assert solution("-1") == -1
