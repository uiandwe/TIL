def merge(leftList, rightList):
    result = []
    while len(leftList) > 0 and len(rightList):
        if leftList[0] <= rightList[0]:
            result.append(leftList.pop(0))
        else:
            result.append(rightList.pop(0))
    while len(leftList) > 0:
        result.append(leftList.pop(0))
    while len(rightList) > 0:
        result.append(rightList.pop(0))

    return result


def merge_sort(list):
    if len(list) <= 1:
        return list

    mid = len(list) // 2
    leftList = list[:mid]
    rightList = list[mid:]
    leftList = merge_sort(leftList)
    rightList = merge_sort(rightList)

    return merge(leftList, rightList)


a = [9,8,7,6,5,4,3,2,1,10]

print merge_sort(a)


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




