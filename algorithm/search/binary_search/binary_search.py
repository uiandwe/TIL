def bs(array, n):

    left = 0
    right = len(array)-1

    while left <= right:
        mid = (left+right) // 2
        if array[mid] == n:
            return mid
        elif array[mid] < n:
            left = mid + 1
        else:
            right = mid - 1

    return -1
