
ret_min = float('inf')
ret_max = float('-inf')
numbers = []
oprations = []


def dfs(result, count):
    global numbers, ret_min, ret_max, oprations
    if count == len(numbers) -1:
        if ret_min > result:
            ret_min = result
        if ret_max < result:
            ret_max = result

    for i in range(4):
        if oprations[i] != 0:
            oprations[i] -= 1
            if i == 0:
                dfs(result + numbers[count + 1], count + 1)
            elif i == 1:
                dfs(result - numbers[count + 1], count + 1)
            elif i == 2:
                dfs(result * numbers[count + 1], count + 1)
            elif i == 3:
                dfs(int(result / numbers[count + 1]), count + 1)
            oprations[i] += 1


def solution(nums, ops):
    global numbers, oprations
    oprations = ops
    numbers = nums

    dfs(nums[0], 0)

    print(ret_max, ret_min)


solution([5, 6], [0, 0, 1, 0])
solution([3, 4, 5], [1, 0, 1, 0])
solution([1, 2, 3, 4, 5, 6], [2, 1, 1, 1])

