import sys

def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp
    return arr

def nextPermutation(arr):
    swapIndex1 = 0
    for i in range(len(arr)-1, 0, -1):
        if arr[i] > arr[i-1]:
            swapIndex1 = i-1
            break

    swapIndex2 = sys.maxsize
    for i in range(len(arr)-1, swapIndex1, -1):
        if arr[i] > arr[swapIndex1] and swapIndex2 > arr[i]:
            swapIndex2 = i
            break

    arr = swap(arr, swapIndex1, swapIndex2)

    return arr[:swapIndex1+1]+sorted(arr[swapIndex1+1:])


def solution(array):
    arr1 = nextPermutation(array)
    print(arr1)
    print(nextPermutation(arr1))

solution([1, 3, 5, 4, 4])
