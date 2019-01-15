def solution(array):
    len_array = len(array)
    more_array = 2
    d = [[0 for x in range(2)] for y in range(len_array+more_array)]

    for i in range(more_array, len(d)):
        d[i][0] = array[i - more_array][0] + max(d[i - 2][0], d[i - 2][1], d[i - 1][1])
        d[i][1] = array[i - more_array][1] + max(d[i - 2][0], d[i - 2][1], d[i - 1][0])

    for i in d:
        print(i)

    return max(d[len_array+more_array-1])
