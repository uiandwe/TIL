

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
