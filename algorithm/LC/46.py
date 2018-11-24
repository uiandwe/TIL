

def backtrack(tempArray, array, d):
    if len(array) == len(tempArray):
        d.append(''.join(str(e) for e in tempArray))
        return

    for i in array:
        if i not in tempArray:
            tempArray.append(i)
            backtrack(tempArray, array, d)
            tempArray.pop(len(tempArray)-1)


def solution(array):
    d = []
    backtrack([], array, d)
    print(d)


solution([1,2,3])
