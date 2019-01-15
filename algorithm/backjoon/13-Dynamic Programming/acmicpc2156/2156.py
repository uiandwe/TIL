def solution(arr):
    d = [[0 for x in range(3)] for y in range(len(arr)+1)]

    for i in range(1, len(arr)+1):
        d[i][0] = max(d[i-1][0], d[i-1][1], d[i-1][2])
        d[i][1] = d[i-1][0]+arr[i-1]
        d[i][2] = d[i-1][1]+arr[i-1]

    return max(d[len(d)-1])
