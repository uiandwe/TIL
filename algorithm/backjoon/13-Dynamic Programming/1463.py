def solution(n):

    d = [0 for x in range(20)]
    d[1] = d[2] = d[3] = 1

    for i in range(4, n+1):
        d[i] = d[i-1] + 1
        if i % 2 == 0:
            d[i] = min(d[i], d[int(i/2)]+1)
        if i % 3 == 0:
            d[i] = min(d[i], d[int(i/3)]+1)

    print(d, d[n])



solution(2)
solution(10)
