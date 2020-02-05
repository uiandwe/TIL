# -*- coding: utf-8 -*-
def solution(array):
    if len(array) <= 1:
        return array


    mid = len(array) // 2

    g1 = solution(array[:mid])
    g2 = solution(array[mid:])

    result = []

    while g1 and g2:
        if g1[0] < g2[0]:
            if g1[0] <= 0 :
                g1.pop(0)
                continue

            result.append(g1.pop(0))
        else:
            result.append(g2.pop(0))


    while g1:
        result.append(g1.pop(0))

    while g2:
        result.append(g2.pop(0))


    return result

print(solution([1,2,3,0,0,0] + [2,5,6]))
