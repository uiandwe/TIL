# -*- coding: utf-8 -*-
def bubble_sort(array):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]

    return array


assert bubble_sort([5, 1, 8, 2]) == [1, 2, 5, 8]
assert bubble_sort([9,1,6,8,4,3,2,0]) == [0,1,2,3,4,6,8,9]

