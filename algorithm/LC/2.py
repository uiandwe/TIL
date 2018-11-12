def solution(array, target):
    dict = {}
    for i in range(len(array)):
        if target-array[i] in dict:
            return [dict[target-array[i]], i]
        else:
            dict[array[i]] = i

print(solution([2, 7, 11, 15], 9))
