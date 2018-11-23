def solution(array):
    cnt = x = 0
    for i in array:
        if cnt == 0:
            x = i
            cnt += 1
        elif x == i:
            cnt += 1
        else:
            cnt -= 1

    return x


print(solution([3, 2, 3]))
print(solution([2, 2, 2, 1, 1, 1, 2, 2]))
