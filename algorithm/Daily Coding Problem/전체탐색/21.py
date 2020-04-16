# -*- coding: utf-8 -*-
def candies(n, arr):
    d = [1 for x in arr]

    for i in range(1, len(arr)):
        if arr[i-1] < arr[i]:
            d[i] = d[i-1] + 1
        elif arr[i-1] > arr[i] and d[i-1] <= d[i]:
            d[i-1] += 1

    for i in reversed(range(1, len(arr))):
        if arr[i-1] > arr[i] and d[i-1] <= d[i]:
            d[i - 1] = d[i] + 1

    return sum(d)


assert candies(3, [1, 2, 2]) == 4

assert candies(10, [2, 4, 2, 6, 1, 7, 8, 9, 2, 1]) == 19
assert candies(8, [2, 4, 3, 5, 2, 6, 4, 5]) == 12
n = 10
assert candies(n, [x for x in reversed(range(1, n+1))]) == 55
n = 100
assert candies(n, [x for x in reversed(range(1, n+1))]) == 5050
n = 10000
assert candies(n, [x for x in reversed(range(1, n+1))]) == 50005000
