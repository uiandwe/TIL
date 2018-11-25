def checkNode(index, i, array):
    if index < len(array) and array[index] is not None:
        if index % 2 == 0 and array[i] > array[index]:
            return False
        elif index % 2 == 1 and array[i] < array[index]:
            return False
    return True


def solution(array):
    for i in range(len(array)):
        if checkNode(2 * i + 1, i,  array) & checkNode(2 * i + 2, i,  array) is False:
            return "False"
    return "True"

print(solution([2, 1, 3]))
print(solution([5, 1, 4, None, None, 3, 6]))
