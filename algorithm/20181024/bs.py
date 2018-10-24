def bs(array, val):
    first = 0
    last = len(array)

    while first<=last:
        mid = (first+last) //2

        if array[mid] == val:
            return mid
        elif array[mid] < val:
            first = mid+1
        else:
            last = mid-1

    return -1


print bs(a, 1)
