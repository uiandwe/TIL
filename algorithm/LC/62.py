

def solution(m, n):
    d = []
    
    for i in range(n):
        temp = []
        for j in range(m):
            temp.append(0)
        d.append(temp)

    for i in range(m):
        d[0][i] = 1

    for i in range(n):
        d[i][0] = 1

    for i in range(1, n):
        for j in range(1, m):
            d[i][j] = d[i-1][j] + d[i][j-1]

    print(d)

solution(3, 2)
solution(7, 3)
