# -*- coding: utf-8 -*-
def solution(brown, red):
    answer = []
    for x in range(1, int(red ** 0.5) + 1):
        if red % x == 0:
            y = red // x

            if 2 * (x + y) == brown - 4:
                answer = [y+2, x+2]
                break
    return answer


assert solution(10, 2) == [4, 3]
assert solution(8, 1) == [3, 3]
assert solution(24, 24) == [8, 6]

print(solution(10, 2))
