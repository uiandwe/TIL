def solution(array, m):

    left = 0
    right = len(array)-1

    while True:
        mid = (left + right)//2
        if array[mid] == m:
            print(mid, array[mid])
            break
        elif array[mid] > m:
            right = mid-1
        else:
            left = mid+1




solution([1, 4, 5, 7, 8, 9, 10, 14, 16, 19, 22, 25, 28, 35, 47, 70], 22)
