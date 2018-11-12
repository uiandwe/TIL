def solution(array):
    dict = {}
    for i in array:
        if i not in dict:
            dict[i] = 1
        else:
            del dict[i]

    return list(dict.keys())


print(solution([2, 2, 1]))
print(solution([4, 2, 1, 2, 1]))
