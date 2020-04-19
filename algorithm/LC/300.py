# LIS n^2

def solution(array):
    d = [1 for x in array]

    for i in range(1, len(array)):
        for j in range(i):
            if array[i] > array[j] and d[j]+1 > d[i]:
                d[i] = d[j] + 1

    return max(d)




assert solution([10, 9, 2, 3, 6, 5, 7, 101, 20]) == 5
assert solution([10,9,2,5,3,7,101,18]) == 4