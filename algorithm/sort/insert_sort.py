# -*- coding: utf-8 -*-
def ins_sort(a):
    n = len(a)

    for i in range(1, n):
        key = a[i]

        j = i-1
        while j >=0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key

    return a
a = [2, 4, 5, 1, 3]
print(ins_sort(a))


def insert_sort(array):

    for i in range(1, len(array)):
        now = array[i]
        j = i-1
        while j >= 0 and array[j] > now:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = now
    return array

assert insert_sort([5, 1, 8, 2]) == [1, 2, 5, 8]
assert insert_sort([9,1,6,8,4,3,2,0]) == [0,1,2,3,4,6,8,9]

