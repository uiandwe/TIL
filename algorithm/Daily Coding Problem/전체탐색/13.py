# -*- coding: utf-8 -*-
"""
Given two strings A and B,

return whether or not A can be shifted some number of times to get B.

For example, if A is abcde and B is cdeab, return true.

If A is abc and B is acb, return false.
"""

def can_shift(target, string):
    return \
        target and string and \
        len(target) == len(string) and \
        string in target * 2


assert can_shift("abcde", "cdeab")
assert not can_shift("abc", "acb")
