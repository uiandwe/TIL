# -*- coding: utf-8 -*-
"""
Given a sorted list of integers, square the elements and give the output in sorted order.

For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].

"""
def solution(array):
    return sorted(list(map(lambda x: x**2 , array)))


assert solution([-9, -2, 0, 2, 3]) == [0, 4, 4, 9, 81]
