def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


def perm3(array):
    a = len(array)-2
    while  a >= 0 and array[a] >= array[a+1]:
        a -=1

    if a != -1:
        b = len(array)-1
        while array[a] >= array[b]:
            b -= 1
        swap(array, a, b)

    print(array[:a+1] + sorted(array[a+1:]))


def solution():

    perm3([1, 3, 5, 4, 4])

solution()
