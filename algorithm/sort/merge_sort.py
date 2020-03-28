# -*- coding: utf-8 -*-
def merge_sort(a):
    n = len(a)

    if n <= 1:
        return a

    mid = n // 2

    g1 = merge_sort(a[:mid])
    g2 = merge_sort(a[mid:])

    result = []

    while g1 and g2:
        if g1[0] < g2[0]:
            result.append(g1.pop(0))
        else:
            result.append(g2.pop(0))

    while g1:
        result.append(g1.pop(0))

    while g2:
        result.append(g2.pop(0))

    return result


a = [9, 8, 7, 6, 5]
print(merge_sort(a))


def merge_s(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2

    m1 = merge_s(array[:mid])
    m2 = merge_s(array[mid:])

    result = []
    while m1 and m2:
        if m1[0] < m2[0]:
            result.append(m1.pop(0))
        else:
            result.append(m2.pop(0))

    while m1:
        result.append(m1.pop(0))

    while m2:
        result.append(m2.pop(0))

    return result


assert merge_s([5, 1, 8, 2]) == [1, 2, 5, 8]
assert merge_s([9,1,6,8,4,3,2,0]) == [0,1,2,3,4,6,8,9]




def merge_sort1(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2

    m1 = merge_sort1(array[mid:])
    m2 = merge_sort1(array[:mid])


    result = []

    while m1 and m2:
        if m1[0] < m2[0]:
            result.append(m1.pop(0))
        else:
            result.append(m2.pop(0))


    while m1:
        result.apend(m1.pop(0))
    while m2:
        result.append(m2.pop(0))

    return result


assert merge_sort1([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]