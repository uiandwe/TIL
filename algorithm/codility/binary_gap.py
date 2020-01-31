# -*- coding: utf-8 -*-
def solution(b):
    if b <= 4:
        return 0
    str_binary = "{0:b}".format(b)

    first = str_binary.find('1')
    last = str_binary.rfind('1')

    str_binary = str_binary[first:last+1]

    temp_binary = str_binary.split("1")
    if len(temp_binary) <= 2:
        return 0

    max_length = 0
    for i in temp_binary:
        max_length = max(max_length, len(i))

    return max_length


assert solution(1041) == 5
assert solution(32) == 0
assert solution(0) == 0
assert solution(1) == 0
assert solution(2) == 0
assert solution(3) == 0
assert solution(4) == 0
assert solution(5) == 1
assert solution(6) == 0
assert solution(7) == 0
assert solution(8) == 0
assert solution(9) == 2
assert solution(10) == 1
