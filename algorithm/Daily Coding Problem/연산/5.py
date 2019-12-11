def get_largest(arr):
    d = [[0, 0] for i in arr]
    d[0][1] = d[0][0] = arr[0]

    for i in range(1, len(arr)):
        d[i][0] = max(d[i - 1][0] * arr[i], arr[i], d[i - 1][1] * arr[i])
        d[i][1] = min(d[i - 1][1] * arr[i], arr[i], d[i - 1][0] * arr[i])

    return max(d[len(d)-1])


assert get_largest([-10, -10, 5, 2]) == 1000
assert get_largest([-10, 10, 5, 2]) == 100
