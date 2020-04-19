def solution(n):
    d = [[1 for x in range(10)] for y in range(2)]

    for i in range(1, n):
        for j in range(1, 10):
            d[1][j] = d[1][j-1] + d[0][j]

        for j in range(10):
            d[0][j] = d[1][j]

    for i in d:
        print(i)

    print(sum(d[0]))

solution(1)
solution(2)
solution(3)
solution(4)

