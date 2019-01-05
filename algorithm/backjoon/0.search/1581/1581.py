def solution(n, m, array):

    left = 0
    right = 2000000000
    t = 0
    cnt = 0
    while left < right:
        mid = (left+right) // 2
        cnt = len(array)
        for i in array:
            cnt += mid//i
        if cnt >= n:
            t = mid-1
            right = mid-1
        else:
            left = mid+1

    for i in range(len(array)):
        print(t, cnt)
        if t % array[i] == 0:
            cnt += 1

        if cnt == n:
            return i + 1
