def solution(n):
    d = [[0 for x in range(10)] for y in range(2)]
    for i in range(1, 10):
        d[0][i] = 1

    for i in range(1, n):
        for j in range(10):
            if j == 0:
                d[i][0] = d[i][j+1]
            elif 1 <= j < 9:
                d[i][j] = d[i-1][j-1] + d[i-1][j+1]
            else:
                d[i][9] = d[i][j-1]

        for j in range(10):
            d[i-1][j] = d[i][j]

    for i in d:
        print(i)

    print(sum(d[0]))

solution(1)