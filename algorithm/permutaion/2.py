def perm2(array, i):
    if len(array) == i:
        print(array)

    for j in range(i, len(array)):
        array[i], array[j] = array[j], array[i]
        perm2(array, i+1)
        array[i], array[j] = array[j], array[i]

def solution():
    perm2([x+1 for x in range(3)], 0)

solution()
