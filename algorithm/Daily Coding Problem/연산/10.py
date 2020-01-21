# -*- coding: utf-8 -*-
"""

Given an unsigned 8-bit integer, swap its even and odd bits. 

The 1st and 2nd bit should be swapped, 

the 3rd and 4th bit should be swapped, and so on.

For example, 10101010 should be 01010101. 11100010 should be 11010001.

"""

def swap_bits(num):
    return ((num & 85) << 1) | ((num & 170) >> 1)


assert swap_bits(255) == 255
assert swap_bits(210) == 225
assert swap_bits(85) == 170
assert swap_bits(170) == 85
assert swap_bits(226) == 209
