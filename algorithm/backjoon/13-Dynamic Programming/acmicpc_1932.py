inputData = [
    [7],
    [3, 8],
    [8, 1, 0],
    [2, 7, 4, 4],
    [4, 5, 2, 6, 5]
]

def solution(arr):
    for i in range(1, len(arr)):
        for j in range(len(arr[i])):
            a1 = a2 = 0
            if j-1 < 0:
                a1 = 0
            else:
                a1 = arr[i-1][j-1]

            if j >= len(arr[i-1]):
                a2 = 0
            else:
                a2 = arr[i-1][j]

            arr[i][j] += max(a1, a2)

    return max(arr[len(arr)-1])


print(solution(inputData))
