def qSort(array):

    if len(array) <= 1:
        return array

    pivot = array[len(array)//2]
    less = []
    equal = []
    more = []

    for i in array:
        if i == pivot:
            equal.append(i)
        elif i < pivot:
            less.append(i)
        else:
            more.append(i)

    return qSort(less) + equal + qSort(more)


def binarySearcy(array, val):

    left = 0
    right = len(array)-1

    while left <= right:
        mid = (left+right) // 2
        if array[mid] == val:
            return mid
        elif array[mid] < val:
            left = mid + 1
        else:
            right = mid -1

    return -1


def solution(n, array):
    array = qSort(array)
    return binarySearcy(array, n)

