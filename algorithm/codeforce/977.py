def solution(n, k):
    for i in range(k):
        if n%10 == 0:
            n = int(n/10)
        else:
            n -= 1

    print(n)

solution(512, 4)
solution(10000000000, 9)


