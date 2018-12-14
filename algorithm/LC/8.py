def solution(numbers, target):
    numbers.sort()
    returnTemp = []

    for i in range(len(numbers)-2):
        partial_target = target-numbers[i]
        j = i+1
        k = len(numbers)-1

        while j < k:
            partial_sum = numbers[j] + numbers[k]
            if partial_sum == partial_target:
                returnTemp.append((numbers[i], numbers[j], numbers[k]))
                break
            elif partial_sum > partial_target:
                k -= 1
            else:
                j += 1

    return returnTemp


print(solution([19, 3, 7, 10, 11], 20))
print(solution([20, 3, 4, 5, 6, 7, 1, 2], 26))
