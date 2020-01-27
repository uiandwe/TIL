def q(a):
    if len(a) <= 1:
        return a

    pivot = a[len(a) // 2]
    less = []
    equal = []
    more = []

    for i in a:
        if i > pivot:
            more.append(i)
        elif i < pivot:
            less.append(i)
        else:
            equal.append(i)

    return q(less)+ equal + q(more)



a = [5, 4, 6, 100, 9, 8, 1, 24, 63, 12]

print q(a)


# -*- coding: utf-8 -*-
def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[len(array)//2]
    less = []
    more = []
    equal = []

    for a in array:
        if a < pivot:
            less.append(a)
        elif a > pivot:
            more.append(a)
        else:
            equal.append(a)

    return quick_sort(less) + equal + quick_sort(more)


assert quick_sort([5, 1, 8, 2]) == [1, 2, 5, 8]
assert quick_sort([9,1,6,8,4,3,2,0]) == [0,1,2,3,4,6,8,9]
