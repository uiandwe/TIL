def b(array, val):
    first = 0
    last = len(array)

    while first <= last :
        mid = (first+last)//2

        if array[mid] == val:
            return mid
        elif array[mid] > val:
            last = mid-1
        else:
            first = mid+1

    return -1


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print b(a, 10)
