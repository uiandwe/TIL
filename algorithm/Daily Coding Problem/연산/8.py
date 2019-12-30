# -*- coding: utf-8 -*-
"""
Implement division of two positive integers without using the division, multiplication, or modulus operators.

Return the quotient as an integer, ignoring the remainder.
"""

def divide(dividend, divisor):
    if not divisor:
        return

    share = 0
    copy_divisor = divisor
    while dividend >= divisor:
        divisor += copy_divisor
        share += 1

    return share


assert not divide(1, 0)
assert divide(1, 1) == 1
assert divide(0, 1) == 0
assert divide(12, 3) == 4
assert divide(13, 3) == 4
assert divide(25, 5) == 5
assert divide(25, 7) == 3
