

def solution(array):

    for i in range(1, len(array)):
        min = 999
        index = i
        for j in range(i, len(array)):
            if min > array[j]:
                min = array[j]
                index = j

        temp = array[i]
        array[i] = array[index]
        array[index] = temp

    return array

a = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
print(solution(a))


def select_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i+1, len(array)):
            if array[min_index] > array[j]:
                min_index = j

        if i != min_index:
            array[i], array[min_index] = array[min_index], array[i]

    return array


assert select_sort([5, 1, 8, 2]) == [1, 2, 5, 8]
assert select_sort([9,1,6,8,4,3,2,0]) == [0,1,2,3,4,6,8,9]

