def solution(array):

    array.sort(key=lambda x: x[0])

    d = []
    for a in range(1, len(array)):
        if array[a-1][1] >= array[a][0]:
            array[a][0] = array[a - 1][0]
            if array[a-1][1] > array[a][1]:
                array[a][1] = array[a-1][1]
        else:
            d.append(array[a-1])

    d.append(array[-1])

    print(d)




solution([[1, 3], [2, 6], [8, 10], [15, 18]])
solution([[1, 4], [4, 6], [2, 3]])
