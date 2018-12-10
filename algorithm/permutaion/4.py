array = []
pick = []
def perm1(pos, i):
    if len(pick) == i:
        print(pick)
        return

    for j in range(pos, len(array)):
        pick.append(array[j])
        perm1(j+1, i)
        pick.pop()



def perm2(pArray, i):
    if len(pArray) == i:
        print(pArray)
    else:
        for j in range(i, len(pArray)):
            pArray[i], pArray[j] = pArray[j], pArray[i]
            perm2(pArray, i+1)
            pArray[i], pArray[j] = pArray[j], pArray[i]


def swap(array, a, b):
    temp = array[a]
    array[a] = array[b]
    array[b] = temp

def next_pu(array):

    a = len(array)-2
    while a>=0 and array[a] >= array[a+1]:
        a -= 1

    if a != -1:
        b = len(array)-1
        while array[a] >= array[b]:
            b -= 1

        swap(array, a, b)

        array = array[:a+1]+sorted(array[a+1:])

    print(array)


def solution():
    global array
    array = [x+1 for x in range(3)]
    perm1(0, 3)

    perm2(array, 0)

    next_pu([1, 3, 5, 4, 4])
    next_pu([1, 2, 3])

solution()
